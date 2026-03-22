import unittest
import os
from report import write_quality_report

class TestReport(unittest.TestCase):
    def test_write_quality_report(self):
        report_path = "test_quality_report.md"
        issue_counts = {"missing_email": 2, "duplicate_email": 1}
        write_quality_report(report_path, 15, 3, issue_counts)
        
        self.assertTrue(os.path.exists(report_path))
        with open(report_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        self.assertIn("Total Rows Processed:** 18", content)
        self.assertIn("Valid Rows:** 15", content)
        self.assertIn("Invalid Rows:** 3", content)
        self.assertIn("- **missing_email:** 2", content)
        self.assertIn("- **duplicate_email:** 1", content)
        
        if os.path.exists(report_path):
            os.remove(report_path)

if __name__ == '__main__':
    unittest.main()
