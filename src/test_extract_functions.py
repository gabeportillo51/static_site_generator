import unittest
from extract_functions import extract_markdown_images, extract_markdown_links

class TestExtractFunctions(unittest.TestCase):
    def test_1(self):
        result_1 = extract_markdown_links("hello [to youtube](https://www.youtube.com) fuck you [to bootdev](https://www.bootdev.com) goodbye")
        result_2 = extract_markdown_links("hello [to youtube](https://www.youtube.com) fuck you [to bootdev](https://www.bootdev.com) goodbye")
        self.assertEqual(result_1, result_2)

    def test_2(self):
        result_1 = extract_markdown_links("hello fuck you [to bootdev](https://www.bootdev.com) goodbye")
        result_2 = extract_markdown_links("hello [to youtube](https://www.youtube.com) fuck you [to bootdev](https://www.bootdev.com) goodbye")
        self.assertNotEqual(result_1, result_2)

    def test_3(self):
        result_1 = extract_markdown_images("hello ![to youtube](https://www.youtube.com) fuck you ![to bootdev](https://www.bootdev.com) goodbye")
        result_2 = extract_markdown_images("hello ![to youtube](https://www.youtube.com) fuck you ![to bootdev](https://www.bootdev.com) goodbye")
        self.assertEqual(result_1, result_2)

    def test_4(self):
        result_1 = extract_markdown_images("hello fuck you ![to bootdev](https://www.bootdev.com) goodbye")
        result_2 = extract_markdown_images("hello ![to youtube](https://www.youtube.com) fuck you ![to bootdev](https://www.bootdev.com) goodbye")
        self.assertNotEqual(result_1, result_2)


if __name__ == "__main__":
    unittest.main()