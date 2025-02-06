import unittest
from leafnode import LEAFNODE

class TestLeafNode(unittest.TestCase):
    def test_1(self):
        node_1 = LEAFNODE("p", "The oven is working properly")
        node_2 = LEAFNODE("p", "The oven is working properly")
        self.assertEqual(node_1, node_2)

    def test_2(self):
        node_1 = LEAFNODE("a", "The oven is working properly", {"href":"https://www.youtube.com", "target": "yellow"})
        node_2 = LEAFNODE("a", "The oven is working properly", {"href":"https://www.youtube.com", "target": "yellow"})
        self.assertEqual(node_1, node_2)

    def test_3(self):
        node_1 = LEAFNODE(None, "The oven is working properly")
        node_2 = LEAFNODE(None, "The oven is working properly")
        self.assertEqual(node_1, node_2)

    def test_4(self):
        node_1 = LEAFNODE("h1", "The oven is working properly")
        node_2 = LEAFNODE("p", "The oven is working properly")
        self.assertNotEqual(node_1, node_2)

    def test_5(self):
        node_1 = LEAFNODE("p", "The oven is not working properly")
        node_2 = LEAFNODE("p", "The oven is working properly")
        self.assertNotEqual(node_1, node_2)

    def test_6(self):
        node_1 = LEAFNODE("a", "The oven is working properly", {"href":"https://www.youtube.com", "target": "yellow"})
        node_2 = LEAFNODE("a", "The oven is working properly", {"href":"https://www.youtube.com"})
        self.assertNotEqual(node_1, node_2)






if __name__ == "__main__":
    unittest.main()