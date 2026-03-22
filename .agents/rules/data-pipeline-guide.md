---
trigger: always_on
---

- main.py is the entry point and demo surface only.
- Do not place transformation logic in main.py.
- Keep parsing, normalization, validation, and reporting in separate modules.
- Keep functions focused and easy to test.
- Make output files explicit and predictable.