import csv
from typing import List, Dict

def read_csv(filename: str) -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_csv(filename: str, data: List[Dict[str, str]], fieldnames: List[str]) -> None:
    """
    Writes a list of dictionaries to a CSV file using the provided field names.
    """
    with open(filename, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
