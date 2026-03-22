"""
Main Entry Point for the Pipeline.
"""
import argparse
import os
import sys
from typing import Dict

# Import components as per the architecture guidelines
from csv_parser import read_csv, write_csv
from cleaner import normalize_row
from validator import validate_row
from report import write_quality_report

def main() -> None:
    """
    Orchestrates the Version 2 pipeline:
    1. Read the input raw data
    2. Format and clean rows
    3. Validate and separate valid/invalid rows
    4. Write the transformed data to individual files
    5. Write a markdown quality report
    """
    parser = argparse.ArgumentParser(description="Process and normalize registration CSV data.")
    parser.add_argument("--input", default="registrations_raw.csv",
                        help="Path to the input CSV file. Defaults to 'registrations_raw.csv'.")
    parser.add_argument("--output-dir", default=".",
                        help="Directory to save the output files. Defaults to the current directory.")
    args = parser.parse_args()

    input_file = args.input
    # Fallback in case of filename variations for the default input
    if input_file == "registrations_raw.csv" and not os.path.exists(input_file) and os.path.exists("registration_raw.csv"):
        input_file = "registration_raw.csv"
        
    out_dir = args.output_dir
    if out_dir != ".":
        os.makedirs(out_dir, exist_ok=True)
        
    cleaned_file = os.path.join(out_dir, "cleaned_registrations.csv")
    review_file = os.path.join(out_dir, "review_needed.csv")
    report_file = os.path.join(out_dir, "quality_report.md")
    
    # 1. Read
    try:
        raw_rows = read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: Could not find '{input_file}'.")
        sys.exit(1)
        
    if not raw_rows:
        print("No data found to process.")
        sys.exit(0)
        
    # 2 & 3. Normalize & Validate
    valid_rows = []
    invalid_rows = []
    seen_emails = set()
    issue_counts: Dict[str, int] = {}
    
    for row in raw_rows:
        normalized = normalize_row(row)
        is_valid, issue = validate_row(normalized, seen_emails)
        if is_valid:
            valid_rows.append(normalized)
        else:
            normalized["issue"] = issue
            invalid_rows.append(normalized)
            issue_counts[issue] = issue_counts.get(issue, 0) + 1
            
    # Extra check if there are columns (from first row)
    fieldnames = []
    if raw_rows:
        # Strip issue if it somehow sneaks into raw columns, though normalize_row doesn't add it
        base_fieldnames = list(normalize_row(raw_rows[0]).keys())
        fieldnames = [f for f in base_fieldnames if f != "issue"]
        
    invalid_fieldnames = fieldnames + ["issue"]
    
    # 4. Write CSV files
    write_csv(cleaned_file, valid_rows, fieldnames)
    write_csv(review_file, invalid_rows, invalid_fieldnames)
        
    # 5. Report
    write_quality_report(report_file, len(valid_rows), len(invalid_rows), issue_counts)
    print(f"Pipeline complete. Valid rows: {len(valid_rows)}, Invalid rows: {len(invalid_rows)}.")

if __name__ == "__main__":
    main()
