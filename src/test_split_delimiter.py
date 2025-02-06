import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def test_1(self):
        node_1 = TextNode("This is text with a **bold** word in it.", TextType.NORMAL)
        node_2 = TextNode("This is text with a **bold** word in it.", TextType.NORMAL)
        result_1 = split_nodes_delimiter([node_1], "**", TextType.BOLD)
        result_2 = split_nodes_delimiter([node_2], "**", TextType.BOLD)
        self.assertEqual(result_1, result_2)

    def test_2(self):
        node_1 = TextNode("This is not text with a **bold** word in it.", TextType.NORMAL)
        node_2 = TextNode("This is text with a **bold** word in it.", TextType.NORMAL)
        result_1 = split_nodes_delimiter([node_1], "**", TextType.BOLD)
        result_2 = split_nodes_delimiter([node_2], "**", TextType.BOLD)
        self.assertNotEqual(result_1, result_2)

    def test_3(self):
        node_1 = TextNode("This is text with a word in it.", TextType.NORMAL)
        node_2 = TextNode("This is text with a **bold** word in it.", TextType.NORMAL)
        result_1 = split_nodes_delimiter([node_1], "**", TextType.BOLD)
        result_2 = split_nodes_delimiter([node_2], "**", TextType.BOLD)
        self.assertNotEqual(result_1, result_2)

    def test_4(self):
        node_1 = TextNode("This is text with an *italic* word in it.", TextType.NORMAL)
        node_2 = TextNode("This is text with an *italic* word in it.", TextType.NORMAL)
        result_1 = split_nodes_delimiter([node_1], "*", TextType.ITALIC)
        result_2 = split_nodes_delimiter([node_2], "*", TextType.ITALIC)
        self.assertEqual(result_1, result_2)

    def test_5(self):
        node_1 = TextNode("This is not text with an *italic* word in it.", TextType.NORMAL)
        node_2 = TextNode("This is text with an *italic* word in it.", TextType.NORMAL)
        result_1 = split_nodes_delimiter([node_1], "*", TextType.ITALIC)
        result_2 = split_nodes_delimiter([node_2], "*", TextType.ITALIC)
        self.assertNotEqual(result_1, result_2)

    def test_6(self):
        node_1 = TextNode("This is text with an word in it.", TextType.NORMAL)
        node_2 = TextNode("This is text with an *italic* word in it.", TextType.NORMAL)
        result_1 = split_nodes_delimiter([node_1], "*", TextType.ITALIC)
        result_2 = split_nodes_delimiter([node_2], "*", TextType.ITALIC)
        self.assertNotEqual(result_1, result_2)

    def test_7(self):
        node_1 = TextNode("This is text with some `code` in it.", TextType.NORMAL)
        node_2 = TextNode("This is text with some `code` in it.", TextType.NORMAL)
        result_1 = split_nodes_delimiter([node_1], "`", TextType.CODE)
        result_2 = split_nodes_delimiter([node_2], "`", TextType.CODE)
        self.assertEqual(result_1, result_2)

    def test_8(self):
        node_1 = TextNode("This is not some text with some `code` in it.", TextType.NORMAL)
        node_2 = TextNode("This is text with some `code` in it.", TextType.NORMAL)
        result_1 = split_nodes_delimiter([node_1], "`", TextType.CODE)
        result_2 = split_nodes_delimiter([node_2], "`", TextType.CODE)
        self.assertNotEqual(result_1, result_2)

    def test_9(self):
        node_1 = TextNode("This is text with an word in it.", TextType.NORMAL)
        node_2 = TextNode("This is text with an `code` word in it.", TextType.NORMAL)
        result_1 = split_nodes_delimiter([node_1], "`", TextType.CODE)
        result_2 = split_nodes_delimiter([node_2], "`", TextType.CODE)
        self.assertNotEqual(result_1, result_2)



if __name__ == "__main__":
    unittest.main()