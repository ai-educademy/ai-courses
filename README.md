# AI Educademy Public Courses

Public course and blog content for [AI Educademy](https://aieducademy.org), the multilingual AI and software engineering learning platform.

This repo contains public lesson content for the currently open programmes plus the public blog. The product model is freemium: the first lesson of every programme is free on the platform, and full programme access is delivered through AI Educademy Pro at £3.99/month, £29.99/year, or £49.99 lifetime.

## What is included

| Programme | Track | Level | Lessons | Status |
|-----------|-------|-------|---------|--------|
| [AI Seeds](programs/ai-seeds/) | Understanding AI | 1 | 10 | Active |
| [AI Sprouts](programs/ai-sprouts/) | Understanding AI | 2 | 10 | Active |
| [AI Sketch](programs/ai-sketch/) | Craft and Engineering | 1 | 10 | Active |
| [Interview Launchpad](programs/ai-launchpad/) | Career Ready | 1 | 10 | Active |

The private `ai-courses-pro` repo contains subscriber lessons for the paid programmes.

## Languages

Lessons are served through the platform in 11 languages: English, French, Dutch, Hindi, Telugu, Spanish, Portuguese, German, Chinese, Japanese, and Arabic. Some translations are machine assisted and need native speaker review.

## Content structure

```text
blog/
├── en/
├── fr/
└── ...
programs/
├── ai-seeds/
│   ├── program.json
│   └── lessons/
└── ...
```

Each lesson is MDX with frontmatter. Keep frontmatter keys in English, even when the lesson body is translated.

## How to contribute

No coding skills are required for content contributions.

1. Fork the repo.
2. Edit or add content under `programs/<programme>/lessons/` or `blog/<locale>/`.
3. Keep examples accurate and learner friendly.
4. Open a pull request against `main`.

Helpful contributions include corrections, clearer explanations, translation reviews, accessibility improvements in diagrams, and practical examples.

## Related repos

| Repo | Purpose |
|------|---------|
| [`ai-platform`](https://github.com/ai-educademy/ai-platform) | Production Next.js app for [aieducademy.org](https://aieducademy.org) |
| [`ai-ui-library`](https://github.com/ai-educademy/ai-ui-library) | Shared React components and design tokens |
| `ai-courses-pro` | Private Pro lesson content |
| [`ai-educademy/.github`](https://github.com/ai-educademy/.github) | Organisation profile and automation docs |

## Licence

Public course content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Pro content is not part of this repository.
