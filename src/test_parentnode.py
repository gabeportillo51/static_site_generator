import unittest
from parentnode import PARENTNODE
from leafnode import LEAFNODE

class TestParentNode(unittest.TestCase):
    def test_1(self):
        node_1 = PARENTNODE("h1", [LEAFNODE("b", "This is bold text")])
        node_2 = PARENTNODE("h1", [LEAFNODE("b", "This is bold text")])
        self.assertEqual(node_1, node_2)

    def test_2(self):
        node_1 = PARENTNODE("h2", [LEAFNODE("b", "This is bold text"), LEAFNODE("code", "This is code froma website", {"href":"https://www.youtube.com"})])
        node_2 = PARENTNODE("h2", [LEAFNODE("b", "This is bold text"), LEAFNODE("code", "This is code froma website", {"href":"https://www.youtube.com"})])
        self.assertEqual(node_1, node_2)

    def test_3(self):
        node_1 = PARENTNODE("h1", [LEAFNODE("b", "This is bold text")], {"href":"https://www.youtube.com"})
        node_2 = PARENTNODE("h1", [LEAFNODE("b", "This is bold text")], {"href":"https://www.youtube.com"})
        self.assertEqual(node_1, node_2)

    def test_5(self):
        node_1 = PARENTNODE("h1", [LEAFNODE("a", "This is bold text")])
        node_2 = PARENTNODE("h1", [LEAFNODE("b", "This is bold text")])
        self.assertNotEqual(node_1, node_2)

    def test_6(self):
        node_1 = PARENTNODE("h1", [LEAFNODE("b", "This is bold text")])
        node_2 = PARENTNODE("h1", [LEAFNODE("b", "This is italic text")])
        self.assertNotEqual(node_1, node_2)

    def test_7(self):
        node_1 = PARENTNODE("h1", [PARENTNODE("h2", [LEAFNODE("b", "This is bold text")])])
        node_2 = PARENTNODE("h1", [PARENTNODE("h2", [LEAFNODE("b", "This is bold text")])])
        self.assertEqual(node_1, node_2)

    def test_8(self):
        node_1 = PARENTNODE("h1", [LEAFNODE("b", "This is bold text")], {"href":"https://www.youtube.com"})
        node_2 = PARENTNODE("h1", [LEAFNODE("b", "This is italic text")])
        self.assertNotEqual(node_1, node_2)

    def test_9(self):
        node_1 = PARENTNODE("h1", None)
        node_2 = PARENTNODE("h1", None)
        self.assertEqual(node_1, node_2)

    def test_10(self):
        node_1 = PARENTNODE(None, [LEAFNODE("b", "This is bold text")])
        node_2 = PARENTNODE(None, [LEAFNODE("b", "This is bold text")])
        self.assertEqual(node_1, node_2)


if __name__ == "__main__":
    unittest.main()