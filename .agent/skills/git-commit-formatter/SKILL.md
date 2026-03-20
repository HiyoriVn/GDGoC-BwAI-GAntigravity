---
name: git-commit-formatter
description: Formats git commit messages according to Conventional Commits. Use when the user asks to write a commit message, summarize changes for a commit, or commit changes.
---

# Git Commit Formatter Skill

When writing a git commit message, follow Conventional Commits.

Format:
<type>[optional scope]: <description>

Allowed types:
- feat
- fix
- docs
- style
- refactor
- perf
- test
- chore

Instructions:
1. Infer the primary type from the current changes.
2. Add a scope when it is helpful.
3. Write the description in imperative mood.
4. Keep the subject line concise.