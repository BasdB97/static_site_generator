import unittest

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_found(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_found_with_leading_whitespace(self):
        markdown = "   # Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_found_with_trailing_whitespace(self):
        markdown = "# Hello   "
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_found_with_multiple_lines(self):
        markdown = "# Hello\nThis is a paragraph"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_not_found(self):
        markdown = "This is a paragraph"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_extract_title_empty_string(self):
        markdown = ""
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_extract_title_multiple_h1_headers(self):
        markdown = "# Hello\n# World"
        self.assertEqual(extract_title(markdown), "Hello")

if __name__ == "__main__":
    unittest.main()