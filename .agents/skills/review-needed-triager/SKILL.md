---
name: review-needed-triager
description: Use this skill when the user asks to analyze flagged rows, explain review_needed.csv, suggest manual fixes, or prepare a checklist for the ops team.
---

# Review Needed Triager

When this skill is triggered, you must perform the following steps:

1. **Read `review_needed.csv`**: Parse and read the current contents of the `review_needed.csv` file.
2. **Group rows by issue**: Categorize the flagged rows based on the specific issue preventing them from being processed.
3. **Explain each issue**: In plain language, explain what each issue means and why the row was flagged.
4. **Suggest the next manual action**: Provide clear recommendations on how to manually correct the issue for each group.
5. **Create `manual_review_checklist.md`**: Generate a checklist document for the ops team summarizing the issues, counts, and the specific actions they need to take.

## Rules
- **DO NOT** automatically edit `registrations_raw.csv` or `cleaned_registrations.csv`.
- Keep the output and the generated checklist concise and actionable.