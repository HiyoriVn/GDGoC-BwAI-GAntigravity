from typing import Dict
import os

def write_quality_report(report_path: str, valid_count: int, invalid_count: int, issue_counts: Dict[str, int]) -> None:
    """
    Writes a markdown quality report summarizing the processing run.
    """
    total_processed = valid_count + invalid_count
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Data Quality Report\n\n")
        f.write("## Overview\n")
        f.write(f"- **Total Rows Processed:** {total_processed}\n")
        f.write(f"- **Valid Rows:** {valid_count}\n")
        f.write(f"- **Invalid Rows:** {invalid_count}\n\n")
        
        f.write("## Issues Breakdown\n")
        if not issue_counts:
            f.write("No issues found! 🎉\n")
        else:
            for issue, count in sorted(issue_counts.items()):
                f.write(f"- **{issue}:** {count}\n")
