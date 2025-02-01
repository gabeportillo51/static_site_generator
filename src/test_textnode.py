import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_1(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node1, node2)

    def test_2(self):
        node1 = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node1, node2)

    def test_3(self):
        node1 = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node1, node2)

    def test_4(self):
        node1 = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertEqual(node1, node2)

    def test_5(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_6(self):
        node1 = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_7(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
