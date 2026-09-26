#!/usr/bin/env python3
"""Locale integrity gate for lesson MDX.

1. Machine-read frontmatter fields (published, order, duration, difficulty) in
   every translated lesson must equal the English source. Translating
   `published: true` to a native word silently breaks lesson visibility.
2. Lines ADDED since the base ref in hi/te lessons must not contain malformed
   Indic script: a virama followed by a vowel sign, a word starting with a
   dependent vowel sign, or a consonant followed by the independent vowel A.
   These are the fingerprints of letter-by-letter transliteration of English
   ("Claude ोपुस" for Opus), which reads as gibberish to native speakers.
   Added te lines are also checked for word-substitution artefacts, and added
   hi lines for letter-by-letter transliteration of English words, which
   produces long runs of bare consonants ("अपपलिकशनस" for applications).
   Only added lines are checked so older content can be repaired separately
   without blocking unrelated PRs.

Usage: check-locale-integrity.py [BASE_REF]
"""
import glob
import os
import re
import subprocess
import sys

FIELDS = ('published', 'order', 'duration', 'difficulty')
TE = '\u0C3E-\u0C4C\u0C55\u0C56'
HI = '\u093E-\u094C'
MALFORMED = {
    'te': re.compile('\u0C4D[' + TE + ']|(?:^|[\\s(\\-"])[' + TE + '\u0C4D]|[\u0C15-\u0C39]\u0C05'),
    'hi': re.compile('\u094D[' + HI + ']|(?:^|[\\s(\\-"])[' + HI + '\u094D]|[\u0915-\u0939]\u0905'),
}
# Word-substitution artefacts from machine translation: an English suffix
# glued to a Telugu word ("వివరణs"), or a verb followed by a redundant form
# of చేయు ("నిర్వహించు చేస్తుంది", "వాడండి చేస్తుంది").
SUBSTITUTION = {
    'te': re.compile('[\u0C00-\u0C7F\u200c]+(?:s|es|ed|ing)\\b'
                     '|[\u0C00-\u0C7F]+\u0C3F\u0C02\u0C1A\u0C41 (?:చేయ|చేస|చేశ|చేసి|చేద్దాం|చేయండి)'
                     '|[\u0C00-\u0C7F]+(?<!ను)ండి (?:అయిన|చేస|చేయ|చేశ|చేసి|చేద్దాం)'),
}
# Four or more consecutive consonants with no vowel sign, virama or nukta.
# Native Hindi rarely does this; transliterated English ("फ़ुनकशन") always does.
# Genuine words that trip it go in HI_TRANSLIT_OK.
HI_BARE = '[\u0915-\u0939\u0958-\u095F]\u093C?(?![\u093E-\u094D\u0962\u0963\u093C])'
HI_TRANSLIT = re.compile('(?:' + HI_BARE + '){4,}')
HI_TRANSLIT_OK = set('''
    लगभग मतलब उपकरण डेवलपर डेवलपरों डेवलपर्स असहमत सहमत आश्चर्यजनक नामकरण
    समझकर रखकर निकटतम जनरल गड़बड़ पढ़कर चलकर अपघटन नफ़रत शयनकक्ष शयनकक्षों
    वर्गीकरणकर्ता फेरबदल गलतफहमी घटकर धड़कन जमकर बदतर समयबद्ध ताकतवर
    सम्मानजनक सहकर हटकर असमतल समतल ज़बरदस्त नफरत
'''.split())
NUKTA = str.maketrans({'\u093C': None, '\u0958': '\u0915', '\u0959': '\u0916', '\u095A': '\u0917',
                       '\u095B': '\u091C', '\u095C': '\u0921', '\u095D': '\u0922', '\u095E': '\u092B',
                       '\u095F': '\u092F'})
HI_TRANSLIT_OK = {w.translate(NUKTA) for w in HI_TRANSLIT_OK}
errors = []


def frontmatter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---', text, re.S)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            key, _, value = line.partition(':')
            if key.strip() in FIELDS:
                out[key.strip()] = value.strip()
    return out


for en in sorted(glob.glob('programs/*/lessons/en/*.mdx')):
    ref = frontmatter(en)
    lessons = os.path.dirname(os.path.dirname(en))
    for locdir in sorted(glob.glob(lessons + '/*/')):
        path = os.path.join(locdir, os.path.basename(en))
        if locdir.rstrip('/').endswith('/en') or not os.path.exists(path):
            continue
        got = frontmatter(path)
        for key, value in ref.items():
            if got.get(key) != value:
                errors.append(f'{path}: frontmatter {key} is {got.get(key)!r}, English has {value!r}')

base = sys.argv[1] if len(sys.argv) > 1 else None
if base:
    diff = subprocess.run(
        ['git', 'diff', '-U0', f'{base}...HEAD', '--', 'programs/*/lessons/hi/*.mdx', 'programs/*/lessons/te/*.mdx'],
        capture_output=True, text=True, check=True).stdout
    current = None
    for line in diff.splitlines():
        if line.startswith('+++ b/'):
            current = line[6:]
        elif line.startswith('+') and not line.startswith('+++') and current:
            loc = current.split('/')[3]
            m = MALFORMED[loc].search(line)
            if m:
                s = max(0, m.start() - 20)
                errors.append(f'{current}: malformed {loc} script near {line[s:m.end() + 20]!r}')
            m = SUBSTITUTION.get(loc) and SUBSTITUTION[loc].search(line)
            if m:
                s = max(0, m.start() - 20)
                errors.append(f'{current}: word-substitution artefact in {loc} near {line[s:m.end() + 20]!r}')
            if loc == 'hi':
                for word in re.findall('[\u0900-\u097F]+', line):
                    if word.translate(NUKTA) not in HI_TRANSLIT_OK and HI_TRANSLIT.search(word):
                        errors.append(f'{current}: transliterated English in hi: {word!r} '
                                      '(translate it, or add a genuine word to HI_TRANSLIT_OK)')

for e in errors:
    print(f'::error::{e}')
print(f'Locale integrity: {len(errors)} problem(s).')
sys.exit(1 if errors else 0)
