import unittest
from htmlnode import HTMLNODE

class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        node_1 = HTMLNODE("p", "I like the color yellow", None, {"href":"https://www.google.com", "target":"_blank"})
        node_2 = HTMLNODE("p", "I like the color yellow", None, {"href":"https://www.google.com", "target":"_blank"})
        self.assertEqual(node_1, node_2)
    
    def test_2(self):
        node_1 = HTMLNODE("h", "I like the color yellow", None, {"href":"https://www.google.com", "target":"_blank"})
        node_2 = HTMLNODE("p", "I like the color yellow", None, {"href":"https://www.google.com", "target":"_blank"})
        self.assertNotEqual(node_1, node_2)

    def test_3(self):
        node_1 = HTMLNODE("p", "I like the color yellow", None, {"href":"https://www.google.com", "target":"_blank"})
        node_2 = HTMLNODE("p", "I like the color red", None, {"href":"https://www.google.com", "target":"_blank"})
        self.assertNotEqual(node_1, node_2)

    def test_4(self):
        node_1 = HTMLNODE("p", "I like the color yellow", ["a", "b", "c"], {"href":"https://www.google.com", "target":"_blank"})
        node_2 = HTMLNODE("p", "I like the color yellow", None, {"href":"https://www.google.com", "target":"_blank"})
        self.assertNotEqual(node_1, node_2)

    def test_5(self):
        node_1 = HTMLNODE("p", "I like the color yellow", None, None)
        node_2 = HTMLNODE("p", "I like the color yellow", None, {"href":"https://www.google.com", "target":"_blank"})
        self.assertNotEqual(node_1, node_2)

    def test_6(self):
        node_1 = HTMLNODE("p", "I like the color yellow", None, {"href":"https://www.google.com", "target":"_blank"})
        node_2 = HTMLNODE("p", "I like the color yellow", None, {"href":"https://www.google.com", "target":"_blank"})
        node_1_props_to_html = node_1.props_to_html()
        node_2_props_to_html = node_2.props_to_html()
        self.assertEqual(node_1_props_to_html, node_2_props_to_html)

    def test_7(self):
        node_1 = HTMLNODE("h1", "I like the color red", [1,2,3], {"href":"https://www.google.com"})
        node_2 = HTMLNODE("h1", "I like the color red", [1,2,3], {"href":"https://www.google.com"})
        self.assertEqual(node_1, node_2)

    def test_8(self):
        node_1 = HTMLNODE("code", "I like the color 88788", [7,4,5], {"href":"https://www.youtube.com", "target":"_blank"})
        node_2 = HTMLNODE("code", "I like the color 88788", [7,4,5], {"href":"https://www.youtube.com", "target":"_blank"})
        self.assertEqual(node_1, node_2)

if __name__ == "__main__":
    unittest.main()