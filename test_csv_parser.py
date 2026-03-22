import unittest
import os
from csv_parser import read_csv, write_csv

class TestCSVParser(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_data.csv"
        
    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_read_csv(self):
        # Set up a generic input CSV for the happy path
        with open(self.test_filename, "w", encoding="utf-8", newline="") as f:
            f.write("id,name\n1,Alice\n2,Bob\n")
            
        data = read_csv(self.test_filename)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["name"], "Alice")
        self.assertEqual(data[1]["id"], "2")
        
    def test_read_csv_invalid_file(self):
        # Invalid input case: file does not exist
        with self.assertRaises(FileNotFoundError):
            read_csv("nonexistent_file.csv")

    def test_write_csv(self):
        # Happy path for writing CSV
        data = [{"id": "1", "name": "Alice"}]
        write_csv(self.test_filename, data, ["id", "name"])
        
        self.assertTrue(os.path.exists(self.test_filename))
        with open(self.test_filename, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("id,name", content)
            self.assertIn("1,Alice", content)

if __name__ == '__main__':
    unittest.main()
