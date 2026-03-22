import unittest
from unittest.mock import patch
import sys
import os
from io import StringIO
from main import main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.input_file = "test_args_input.csv"
        self.output_dir = "test_args_out"
        self.cleaned_file = os.path.join(self.output_dir, "cleaned_registrations.csv")
        self.review_file = os.path.join(self.output_dir, "review_needed.csv")
        self.report_file = os.path.join(self.output_dir, "quality_report.md")
        
        with open(self.input_file, "w", encoding="utf-8") as f:
            f.write("name,email,ticket_type\nJohn,john@test.com,VIP\n")
            
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.cleaned_file):
            os.remove(self.cleaned_file)
        if os.path.exists(self.review_file):
            os.remove(self.review_file)
        if os.path.exists(self.report_file):
            os.remove(self.report_file)
        if os.path.exists(self.output_dir):
            try:
                os.rmdir(self.output_dir)
            except OSError:
                pass

    @patch('sys.argv', ['main.py', '--input', 'test_args_input.csv', '--output-dir', 'test_args_out'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_happy_path(self, mock_stdout):
        # Happy path testing full app arguments flow
        main()
        self.assertTrue(os.path.exists(self.cleaned_file))
        self.assertTrue(os.path.exists(self.review_file))
        self.assertTrue(os.path.exists(self.report_file))
        
    @patch('sys.argv', ['main.py', '--input', 'nonexistent.csv'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_file_not_found(self, mock_stdout):
        # Invalid input gracefully ends logic
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

    @patch('sys.argv', ['main.py', '--input', 'empty_input.csv', '--output-dir', 'test_args_out'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_empty_data(self, mock_stdout):
        # Another normalization case with missing records
        with open("empty_input.csv", "w", encoding="utf-8") as f:
            pass # an empty file or just headers? Let's just create empty.
        
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)
        
        if os.path.exists("empty_input.csv"):
            os.remove("empty_input.csv")

if __name__ == '__main__':
    unittest.main()
