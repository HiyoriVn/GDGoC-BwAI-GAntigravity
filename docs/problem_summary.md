# Problem Summary

Clean a messy event registration CSV into standardized outputs that are ready for analysis and manual review.

## Context

- Start from provided context, not a blank project.
- Source data is the raw registration export in `registration_raw.csv`.
- The dataset contains inconsistent whitespace, mixed casing, ticket aliases, missing emails, duplicate emails after normalization, and unsupported ticket values.

## Desired Result

Produce a workflow that turns the raw file into:

- `cleaned_registrations.csv`
- `review_needed.csv`
- `quality_report.md`
