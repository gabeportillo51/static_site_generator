import unittest
from parentnode import *
from leafnode import *

class TestPARENTNODE(unittest.TestCase):
    def test_1(self):
        node1 = PARENTNODE("p", [LEAFNODE("b", "Bold text"), 
                         LEAFNODE(None, "Normal text"), 
                         LEAFNODE("i", "italic text"), 
                         LEAFNODE(None, "Normal text")], 
                         props={"href": "https://www.google.com", "target": "_blank"})
        node2 = PARENTNODE("p", [LEAFNODE("b", "Bold text"), 
                         LEAFNODE(None, "Normal text"), 
                         LEAFNODE("i", "italic text"), 
                         LEAFNODE(None, "Normal text")], 
                         props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1, node2)

    def test_2(self):
        node1 = PARENTNODE("p", [LEAFNODE("p", "Bold text"), 
                         LEAFNODE(None, "Normal text"), 
                         LEAFNODE("i", "italic text"), 
                         LEAFNODE(None, "Normal text")], 
                         props={"href": "https://www.google.com", "target": "_blank"})
        node2 = PARENTNODE("p", [LEAFNODE("b", "Bold text"), 
                         LEAFNODE(None, "Normal text"), 
                         LEAFNODE("i", "italic text"), 
                         LEAFNODE(None, "Normal text")], 
                         props={"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node1, node2)

    def test_3(self):
        node1 = PARENTNODE("p", [LEAFNODE("b", "Bold text"), 
                         LEAFNODE(None, "Normal text"), 
                         LEAFNODE("i", "italic text"), 
                         LEAFNODE(None, "Normal text")], 
                         props={"href": "https://www.google.com", "target": "_blank"})
        node2 = PARENTNODE("p", [LEAFNODE("b", "Bold text"), 
                         LEAFNODE(None, "Normal text"), 
                         LEAFNODE("i", "italic text"), 
                         LEAFNODE(None, "Normal text")])
        self.assertNotEqual(node1, node2)

    def test_4(self):
        node1 = PARENTNODE("p", [PARENTNODE("p", [LEAFNODE(None, "Normal text"), LEAFNODE("i", "italic text")]), 
                         LEAFNODE(None, "Normal text"), 
                         LEAFNODE("i", "italic text"), 
                         LEAFNODE(None, "Normal text")], 
                         props={"href": "https://www.google.com", "target": "_blank"})
        node2 = PARENTNODE("p", [PARENTNODE("p", [LEAFNODE(None, "Normal text"), LEAFNODE("i", "italic text")]), 
                         LEAFNODE(None, "Normal text"), 
                         LEAFNODE("i", "italic text"), 
                         LEAFNODE(None, "Normal text")], 
                         props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()

    

    