# Module Plan (Version 1)

## Proposed Python Files

1. **`main.py`**
   - **Responsibility**: Serves as the main entry point and demo surface for the application. It orchestrates the high-level workflow: calling the reader, passing data to the normalizer, calling the writer, and printing the console summary.

2. **`io_operations.py`**
   - **Responsibility**: Handles all file inputs and outputs. For Version 1, this means reading rows from `registrations_raw.csv` and writing the processed rows to `normalized_preview.csv`.

3. **`normalization.py`**
   - **Responsibility**: Houses the core logic to normalize and format individual rows (e.g., standardizing text casing, formatting dates, stripping whitespace). It will strictly handle transformations without performing validation, rejection, or deduplication yet.

## Why `main.py` should stay small

According to our data pipeline guide, `main.py` functions strictly as the entry point rather than the place for core transformation logic. Keeping `main.py` small and devoid of complex business logic ensures that parsing, normalization, and validation remain in separated, focused modules. This separation of concerns makes individual functions much easier to test and maintains explicit, predictable data flows.
