# Acceptance Criteria

## Input

- Use `registration_raw.csv` as the raw input file.

## Required Outputs

- `cleaned_registrations.csv` contains normalized rows that pass validation.
- `review_needed.csv` contains rows that need manual review.
- `quality_report.md` summarizes what was cleaned and what was flagged.

## Normalization Rules

- Trim surrounding whitespace from text fields.
- Convert names to title case.
- Lowercase emails.
- Normalize ticket aliases to canonical values:
  - `VIP`
  - `Standard`
  - `Student`

## Validation Rules

- Flag rows with a missing email.
- Flag rows with an unknown ticket type after normalization.
- Flag rows with a duplicate normalized email.
