import unittest
from cleaner import trim_whitespace, normalize_ticket_type, normalize_row

class TestCleaner(unittest.TestCase):
    def test_trim_whitespace(self):
        # Happy path
        self.assertEqual(trim_whitespace("  hello  "), "hello")
        self.assertEqual(trim_whitespace("world"), "world")
        
        # Invalid/empty input case
        self.assertEqual(trim_whitespace(None), "")
        self.assertEqual(trim_whitespace("   "), "")

    def test_normalize_ticket_type(self):
        # Normalization cases for known types
        self.assertEqual(normalize_ticket_type("VIP"), "vip")
        self.assertEqual(normalize_ticket_type(" VIP "), "vip")
        self.assertEqual(normalize_ticket_type("vip-pass"), "vip")
        self.assertEqual(normalize_ticket_type("STD"), "standard")
        self.assertEqual(normalize_ticket_type("standard pass"), "standard")
        self.assertEqual(normalize_ticket_type(" student "), "student")
        
        # Unrecognized input case
        self.assertEqual(normalize_ticket_type("unknown-type"), "unknown-type")
        self.assertEqual(normalize_ticket_type("general"), "general")
        
    def test_normalize_row(self):
        # Happy path testing full row transformation
        row = {
            "name": " john doe ",
            "email": "  JOHN@example.COM  ",
            "ticket_type": " VIP-PASS ",
            "company": "  tech inc  "
        }
        expected = {
            "name": "John Doe",
            "email": "john@example.com",
            "ticket_type": "vip",
            "company": "tech inc"
        }
        self.assertEqual(normalize_row(row), expected)

if __name__ == '__main__':
    unittest.main()
