import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_1(self):
        node_1 = TextNode("I have two apples", TextType.NORMAL)
        node_2 = TextNode("I have two apples", TextType.NORMAL)
        self.assertEqual(node_1, node_2)

    def test_2(self):
        node_1 = TextNode("I have two apples", TextType.BOLD)
        node_2 = TextNode("I have two apples", TextType.BOLD)
        self.assertEqual(node_1, node_2)

    def test_3(self):
        node_1 = TextNode("I have two apples", TextType.ITALIC)
        node_2 = TextNode("I have two apples", TextType.ITALIC)
        self.assertEqual(node_1, node_2)

    def test_4(self):
        node_1 = TextNode("I have two apples", TextType.CODE)
        node_2 = TextNode("I have two apples", TextType.CODE)
        self.assertEqual(node_1, node_2)

    def test_5(self):
        node_1 = TextNode("I have two apples", TextType.LINK)
        node_2 = TextNode("I have two apples", TextType.LINK)
        self.assertEqual(node_1, node_2)

    def test_6(self):
        node_1 = TextNode("I have two apples", TextType.IMAGE)
        node_2 = TextNode("I have two apples", TextType.IMAGE)
        self.assertEqual(node_1, node_2)

    def test_7(self):
        node_1 = TextNode("I have two apples", TextType.NORMAL)
        node_2 = TextNode("I have three apples", TextType.NORMAL)
        self.assertNotEqual(node_1, node_2)

    def test_8(self):
        node_1 = TextNode("I have two apples", TextType.BOLD)
        node_2 = TextNode("I have three apples", TextType.BOLD)
        self.assertNotEqual(node_1, node_2)

    def test_9(self):
        node_1 = TextNode("I have two apples", TextType.ITALIC)
        node_2 = TextNode("I have three apples", TextType.ITALIC)
        self.assertNotEqual(node_1, node_2)

    def test_10(self):
        node_1 = TextNode("I have two apples", TextType.CODE)
        node_2 = TextNode("I have three apples", TextType.CODE)
        self.assertNotEqual(node_1, node_2)

    def test_11(self):
        node_1 = TextNode("I have two apples", TextType.LINK)
        node_2 = TextNode("I have three apples", TextType.LINK)
        self.assertNotEqual(node_1, node_2)

    def test_12(self):
        node_1 = TextNode("I have two apples", TextType.IMAGE)
        node_2 = TextNode("I have three apples", TextType.IMAGE)
        self.assertNotEqual(node_1, node_2)

    def test_13(self):
        node_1 = TextNode("I have two apples", TextType.NORMAL, url="https://www.youtube.com")
        node_2 = TextNode("I have two apples", TextType.NORMAL)
        self.assertNotEqual(node_1, node_2)

    def test_14(self):
        node_1 = TextNode("I have two apples", TextType.BOLD, url="https://www.youtube.com")
        node_2 = TextNode("I have two apples", TextType.BOLD)
        self.assertNotEqual(node_1, node_2)

    def test_15(self):
        node_1 = TextNode("I have two apples", TextType.ITALIC, url="https://www.youtube.com")
        node_2 = TextNode("I have two apples", TextType.ITALIC)
        self.assertNotEqual(node_1, node_2)

    def test_16(self):
        node_1 = TextNode("I have two apples", TextType.CODE, url="https://www.youtube.com")
        node_2 = TextNode("I have two apples", TextType.CODE)
        self.assertNotEqual(node_1, node_2)

    def test_17(self):
        node_1 = TextNode("I have two apples", TextType.LINK, url="https://www.youtube.com")
        node_2 = TextNode("I have two apples", TextType.LINK)
        self.assertNotEqual(node_1, node_2)

    def test_18(self):
        node_1 = TextNode("I have two apples", TextType.IMAGE, url="https://www.youtube.com")
        node_2 = TextNode("I have two apples", TextType.IMAGE)
        self.assertNotEqual(node_1, node_2)

    def test_19(self):
        node_1 = TextNode("I have two apples", TextType.NORMAL)
        node_2 = TextNode("I have two apples", TextType.NORMAL)
        leafnode_1 = node_1.text_node_to_html_node()
        leafnode_2 = node_2.text_node_to_html_node()
        self.assertEqual(leafnode_1, leafnode_2)

    def test_20(self):
        node_1 = TextNode("I have two apples", TextType.BOLD)
        node_2 = TextNode("I have two apples", TextType.BOLD)
        leafnode_1 = node_1.text_node_to_html_node()
        leafnode_2 = node_2.text_node_to_html_node()
        self.assertEqual(leafnode_1, leafnode_2)

    def test_21(self):
        node_1 = TextNode("I have two apples", TextType.ITALIC)
        node_2 = TextNode("I have two apples", TextType.ITALIC)
        leafnode_1 = node_1.text_node_to_html_node()
        leafnode_2 = node_2.text_node_to_html_node()
        self.assertEqual(leafnode_1, leafnode_2)

    def test_22(self):
        node_1 = TextNode("I have two apples", TextType.IMAGE, url="https://www.youtube.com")
        node_2 = TextNode("I have two apples", TextType.IMAGE, url="https://www.youtube.com")
        leafnode_1 = node_1.text_node_to_html_node()
        leafnode_2 = node_2.text_node_to_html_node()
        self.assertEqual(leafnode_1, leafnode_2)
    
    def test_23(self):
        node_1 = TextNode("I have two apples", TextType.LINK, url="https://www.youtube.com")
        node_2 = TextNode("I have two apples", TextType.LINK, url="https://www.youtube.com")
        leafnode_1 = node_1.text_node_to_html_node()
        leafnode_2 = node_2.text_node_to_html_node()
        self.assertEqual(leafnode_1, leafnode_2)

    def test_24(self):
        node_1 = TextNode("I have two apples", TextType.LINK, url="https://www.youtube.com")
        node_2 = TextNode("I have three apples", TextType.LINK, url="https://www.youtube.com")
        leafnode_1 = node_1.text_node_to_html_node()
        leafnode_2 = node_2.text_node_to_html_node()
        self.assertNotEqual(leafnode_1, leafnode_2)

    def test_25(self):
        node_1 = TextNode("I have two apples", TextType.LINK, url="https://www.youtube.com")
        node_2 = TextNode("I have two apples", TextType.IMAGE, url="https://www.youtube.com")
        leafnode_1 = node_1.text_node_to_html_node()
        leafnode_2 = node_2.text_node_to_html_node()
        self.assertNotEqual(leafnode_1, leafnode_2)

    def test_26(self):
        node_1 = TextNode("I have two apples", TextType.LINK, url="https://www.youtube.com")
        node_2 = TextNode("I have two apples", TextType.LINK, url="https://www.google.com")
        leafnode_1 = node_1.text_node_to_html_node()
        leafnode_2 = node_2.text_node_to_html_node()
        self.assertNotEqual(leafnode_1, leafnode_2)


if __name__ == "__main__":
    unittest.main()