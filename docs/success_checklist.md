# Success Checklist

## Goal

Turn the raw event registration CSV into clean output files plus a clear review queue.

## Input

- `registration_raw.csv`

## Required Outputs

- `cleaned_registrations.csv`
- `review_needed.csv`
- `quality_report.md`

## Normalization Rules

- Trim whitespace.
- Title-case names.
- Lowercase emails.
- Normalize ticket aliases to `VIP`, `Standard`, or `Student`.

## Validation Rules

- Missing email
- Unknown ticket type
- Duplicate normalized email

## End-of-Lab Checklist

- Confirm the workflow starts from the provided CSV and written requirements.
- Confirm `registration_raw.csv` is the input file.
- Confirm `cleaned_registrations.csv` is produced.
- Confirm `review_needed.csv` is produced.
- Confirm `quality_report.md` is produced.
- Confirm names, emails, and ticket types are normalized consistently.
- Confirm missing emails, unknown ticket types, and duplicate normalized emails are flagged for review.
