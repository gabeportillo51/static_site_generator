import unittest
from textnode import TextNode, TextType
from split_functions import split_nodes_image, split_nodes_link

class TestSplitFunctions(unittest.TestCase):
    def test_1(self):
        node_1 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        node_2 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        result_1 = split_nodes_link([node_1])
        result_2 = split_nodes_link([node_2])
        self.assertEqual(result_1, result_2)

    def test_2(self):
        node_1 = TextNode("This is text with a [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        node_2 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        result_1 = split_nodes_link([node_1])
        result_2 = split_nodes_link([node_2])
        self.assertNotEqual(result_1, result_2)

    def test_3(self):
        node_1 = TextNode("This is text with a link and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        node_2 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        result_1 = split_nodes_link([node_1])
        result_2 = split_nodes_link([node_2])
        self.assertNotEqual(result_1, result_2)

    def test_4(self):
        node_1 = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        node_2 = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        result_1 = split_nodes_image([node_1])
        result_2 = split_nodes_image([node_2])
        self.assertEqual(result_1, result_2)

    def test_5(self):
        node_1 = TextNode("This is text with a ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        node_2 = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        result_1 = split_nodes_image([node_1])
        result_2 = split_nodes_image([node_2])
        self.assertNotEqual(result_1, result_2)

    def test_6(self):
        node_1 = TextNode("This is text with a link and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        node_2 = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        result_1 = split_nodes_image([node_1])
        result_2 = split_nodes_image([node_2])
        self.assertNotEqual(result_1, result_2)

    def test_7(self):
        test_case_1 = [TextNode("hello[hello](hello)", TextType.NORMAL), TextNode("hello[hello](hello)", TextType.NORMAL)]
        test_case_2 = [TextNode("hello[hello](hello)", TextType.NORMAL), TextNode("hello[hello](hello)", TextType.NORMAL)]
        result_1 = split_nodes_link(test_case_1)
        result_2 = split_nodes_link(test_case_2)
        self.assertEqual(result_1, result_2)

    def test_8(self):
        test_case_1 = [TextNode("hello", TextType.NORMAL), TextNode("hello[hello](hello)", TextType.NORMAL)]
        test_case_2 = [TextNode("hello[hello](hello)", TextType.NORMAL), TextNode("hello[hello](hello)", TextType.NORMAL)]
        result_1 = split_nodes_link(test_case_1)
        result_2 = split_nodes_link(test_case_2)
        self.assertNotEqual(result_1, result_2)

    def test_9(self):
        test_case_1 = [TextNode("hello![hello](hello)", TextType.NORMAL), TextNode("hello![hello](hello)", TextType.NORMAL)]
        test_case_2 = [TextNode("hello![hello](hello)", TextType.NORMAL), TextNode("hello![hello](hello)", TextType.NORMAL)]
        result_1 = split_nodes_image(test_case_1)
        result_2 = split_nodes_image(test_case_2)
        self.assertEqual(result_1, result_2)

    def test_10(self):
        test_case_1 = [TextNode("hello", TextType.NORMAL), TextNode("hello![hello](hello)", TextType.NORMAL)]
        test_case_2 = [TextNode("hello![hello](hello)", TextType.NORMAL), TextNode("hello![hello](hello)", TextType.NORMAL)]
        result_1 = split_nodes_image(test_case_1)
        result_2 = split_nodes_image(test_case_2)
        self.assertNotEqual(result_1, result_2)

if __name__ == "__main__":
    unittest.main()