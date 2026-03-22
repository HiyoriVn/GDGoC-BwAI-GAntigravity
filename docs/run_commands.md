# CLI Run Commands (Version 1)

This project uses standard Python `argparse` to provide a flexible Command-Line Interface. Below are three examples demonstrating how to use the pipeline.

## 1. Default Run

By default, the script expects an input file named `registrations_raw.csv` in the current directory, processes it, and saves the output as `normalized_preview.csv` also in the current directory.

```bash
python main.py
```

## 2. Custom Input Path

To provide a custom input CSV file entirely (useful if testing other data files or fetching from a specific path), use the `--input` argument:

```bash
python main.py --input data/my_custom_registrations.csv
```

## 3. Custom Output Directory

To specify a structural difference for the output destination, use the `--output-dir` argument. The tool handles missing parent structures implicitly and drops `normalized_preview.csv` directly into it.

```bash
python main.py --output-dir processed_data
```
