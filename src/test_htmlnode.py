import unittest
from htmlnode import *

class TestHTMLNODE(unittest.TestCase):
    def test_1(self):
        node1 = HTMLNODE(tag="h1", value="Hello")
        node2 = HTMLNODE(tag="h1", value="Hello")
        self.assertEqual(node1, node2)
    def test_2(self):
        node1 = HTMLNODE(tag="p", value="Hello")
        node2 = HTMLNODE(tag="h1", value="Hello")
        self.assertNotEqual(node1, node2)
    def test_3(self):
        node1 = HTMLNODE(tag="ul", value="Hello", props="www.youtube.com")
        node2 = HTMLNODE(tag="ul", value="Hello", props="www.youtube.com")
        self.assertEqual(node1, node2)
    def test_4(self):
        node1 = HTMLNODE(tag="h1", value="Hello")
        node2 = HTMLNODE(tag="h1", value="Hey")
        self.assertNotEqual(node1, node2)
    def test_5(self):
        node1 = HTMLNODE(value="Hello")
        node2 = HTMLNODE(tag="h1", value="Hello")
        self.assertNotEqual(node1, node2)
    def test_6(self):
        node = HTMLNODE(props={"href": "https://www.google.com", "target": "_blank"})
        return node.props_to_html()
    


if __name__ == "__main__":
    unittest.main()