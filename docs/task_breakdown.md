# Task Breakdown (Version 1 Scope)

## Implementation Steps

**Step 1: Scaffolding and File Creation**
- Create `main.py`, `io_operations.py`, and `normalization.py`. 
- Set up boilerplate code and basic docstrings following the style guide.

**Step 2: Implement CSV Reader**
- In `io_operations.py`, write a function to read `registrations_raw.csv`.
- Ensure it returns the rows as a manageable data structure (like a list of dictionaries).

**Step 3: Implement Row Normalization**
- In `normalization.py`, write functions that transform a single row's raw values into their normalized forms.
- *Note: Do not implement row deduplication or unsupported ticket type rejection in this step.*

**Step 4: Implement CSV Writer**
- In `io_operations.py`, implement a function that accepts the normalized records and writes them to `normalized_preview.csv`.

**Step 5: Pipeline Orchestration**
- In `main.py`, piece together the pipeline: read the raw file, iterate through the rows to normalize them, and write them to the output file.

**Step 6: Console Summary Output**
- Update `main.py` to keep track of the total number of records processed.
- Print a short, clear console summary upon successful completion.

**Step 7: Verification**
- Run `python main.py` in the terminal.
- Verify that `normalized_preview.csv` is correctly created and the normalized output matches expected formatting. Confirm the console summary displays the correct total row count.
