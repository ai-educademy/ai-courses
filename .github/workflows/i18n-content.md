---
emoji: "🌍"
name: i18n Content
description: Tracks lesson coverage across the 11 locales, finds translation gaps and drift, and flags Arabic RTL issues. Issues for judgement, PRs only for mechanical fixes.
on:
  schedule:
    - cron: "weekly on thursday"
  workflow_dispatch:
max-daily-ai-credits: 6000
permissions:
  contents: read
  pull-requests: read
  issues: read
engine:
  id: gemini
  model: gemini-2.5-flash-lite
timeout-minutes: 25
strict: true
network:
  allowed: [defaults]
tools:
  cli-proxy: true
  edit:
  cache-memory: true
  bash: ["git *", "cat", "ls", "grep", "head", "tail", "find", "wc"]
  github:
    mode: gh-proxy
    toolsets: [repos, issues, pull_requests]
safe-outputs:
  create-pull-request:
  create-issue:
    labels: [content, i18n]
    close-older-issues: true
---

# i18n Content

AI Educademy sells to a global audience in 11 languages. A lesson that exists in English but not in Hindi is a paying learner who cannot use what they paid for. Your job is to map coverage, find gaps and drift, and flag anything that needs a human translator, without ever machine-translating a whole lesson yourself.

## The locales

`en, fr, nl, hi, te, es, pt, de, zh, ja, ar`. English (`en`) is the source of truth. Arabic (`ar`) is right-to-left.

## What to check

Use `find`, `ls`, `grep` and `git log` to build the real picture per programme.

1. **Coverage matrix.** For every English lesson under `programs/<slug>/lessons/en/`, check whether the same lesson slug exists in each of the other 10 locales. Report missing translations as a matrix or a per-locale gap list.
2. **Translation drift.** Compare `git log` dates. Where the English lesson was updated after its translation was last touched, the translation is likely stale. Report these as drift, per lesson per locale.
3. **Frontmatter parity.** Translations should carry the same required frontmatter fields and the same `order` as the English source. Machine-translated files should carry `machineTranslated: true`. Report missing fields, mismatched `order`, and machine-translated files that lack the flag.
4. **Arabic RTL.** In `ar` lessons, flag content that will render badly right-to-left: embedded left-to-right runs without isolation, mirrored punctuation problems, and layout-sensitive markup. Describe the issue; do not attempt to rewrite Arabic prose.
5. **Blog parity.** Apply the same coverage and drift checks to `blog/<locale>/`.

## How to report

- Open an **issue** for the substantive findings: coverage gaps, drift, and RTL problems. One clear issue per locale or per programme, listing exact lesson paths. These need a human translator, so give them a clean worklist.
- Open a **pull request only for mechanical, unambiguous frontmatter fixes**: adding a missing `machineTranslated: true` flag, correcting an `order` value to match the English source, adding a required field that can be copied verbatim (like `icon`). One concern per PR.
- Never machine-translate a lesson body, in whole or in part, and never open a PR that adds translated prose. Translation of teaching content is a human decision.

## Forbidden

- Never translate lesson or blog prose. Ever. Raise an issue instead.
- Never edit `.github/workflows/`.
- Never rewrite Arabic (or any) content to "fix" RTL. Describe the problem in an issue.
- Never claim a locale is complete without having listed the files you checked.
