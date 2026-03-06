<div align="center">

# 🌱 AI Seeds — Level 1: Absolute Beginners

### The first step in your AI journey at [AI Educademy](https://aieducademy.vercel.app)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Languages](https://img.shields.io/badge/languages-5-orange.svg)](#-content-structure)

**No coding. No maths. No prior experience needed.**

[🚀 Start Learning](https://aieducademy.vercel.app/programs/ai-seeds) · [🌍 Translate](#-help-translate) · [📦 Platform Repo](https://github.com/ai-educademy/ai-platform)

---

</div>

## 📋 What is This?

This repo contains the **lesson content** for AI Seeds — the first level of AI Educademy. It's a content-only package consumed by the [`ai-platform`](https://github.com/ai-educademy/ai-platform) app shell via git submodules.

> **Looking for the live site?** Visit [aieducademy.vercel.app](https://aieducademy.vercel.app)
> **Looking for the app code?** See [ai-platform](https://github.com/ai-educademy/ai-platform)
> **Looking for UI components?** See [ai-ui-library](https://github.com/ai-educademy/ai-ui-library)

## 📚 Lessons

| # | Lesson | Duration | Languages |
|---|--------|----------|-----------|
| 1 | What is Artificial Intelligence? | 10 min | 🇬🇧 🇫🇷 🇳🇱 🇮🇳 🇮🇳 |
| 2 | How Machines Learn | 12 min | ��🇧 |
| 3 | Your First AI Model | 15 min | 🇬🇧 |

## 📁 Content Structure

```
program.json                   # Program metadata
lessons/
├── en/                        # English lessons (MDX)
│   ├── what-is-ai.mdx
│   ├── how-machines-learn.mdx
│   └── your-first-ai-model.mdx
├── fr/                        # French
├── hi/                        # Hindi
├── nl/                        # Dutch
└── te/                        # Telugu
```

## ✍️ Writing Lessons

Each lesson is an MDX file with frontmatter:

```mdx
---
title: "What is Artificial Intelligence?"
description: "Discover what AI really means — no jargon."
order: 1
duration: "10 min"
difficulty: "beginner"
image: "/images/lessons/what-is-ai.svg"
---

# What is Artificial Intelligence?

Your lesson content here...
```

## 🌍 Help Translate

We'd love translations! Each lesson lives in a locale folder (`en/`, `fr/`, etc.):

1. Pick a lesson from `lessons/en/`
2. Create the same file under your locale folder (e.g., `es/what-is-ai.mdx`)
3. Translate the content, keeping the frontmatter keys in English
4. Submit a PR

## 🏗️ Part of AI Educademy

| Repo | Description |
|------|-------------|
| [`ai-platform`](https://github.com/ai-educademy/ai-platform) | 🌐 Main Next.js app shell |
| [`ai-ui-library`](https://github.com/ai-educademy/ai-ui-library) | 🎨 Shared design system ([npm](https://www.npmjs.com/package/@ai-educademy/ai-ui-library)) |
| **`ai-seeds`** | 🌱 **Level 1: Absolute beginners** ← you are here |
| `ai-sprouts` | 🌿 Level 2: Foundations (coming soon) |
| `ai-branches` | 🌳 Level 3: Applied AI (coming soon) |
| `ai-canopy` | 🏕️ Level 4: Advanced (coming soon) |
| `ai-forest` | 🌲 Level 5: Expert (coming soon) |

## 📄 License

MIT © [AI Educademy](https://github.com/ai-educademy)
