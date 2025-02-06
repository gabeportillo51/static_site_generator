import unittest
from text_to_textnode import *

class TestTextToTextNode(unittest.TestCase):
    def test_1(self):
        result_1 = text_to_textnode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        result_2 = text_to_textnode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(result_1, result_2)

    def test_2(self):
        result_1 = text_to_textnode("This is with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        result_2 = text_to_textnode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertNotEqual(result_1, result_2)


if __name__ == "__main__":
    unittest.main()
