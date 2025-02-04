import unittest
from leafnode import *

class TestLEAFNODE(unittest.TestCase):
    def test_1(self):
        leaf1 = LEAFNODE("p", "Hello, this is basic text in a paragraph")
        leaf2 = LEAFNODE("p", "Hello, this is basic text in a paragraph")
        self.assertEqual(leaf1, leaf2)

    def test_2(self):
        leaf1 = LEAFNODE("p", "Hello, this is bullshit text in a paragraph")
        leaf2 = LEAFNODE("p", "Hello, this is basic text in a paragraph")
        self.assertNotEqual(leaf1, leaf2)
        
    def test_3(self):
        leaf1 = LEAFNODE("b", "Click Here", props={"href":"https://www.google.com"})
        leaf2 = LEAFNODE("a", "Click Here", props={"href":"https://www.google.com"})
        self.assertNotEqual(leaf1, leaf2)
        
    def test_4(self):
        leaf1 = LEAFNODE("a", "Click Here", props={"href":"https://www.google.com", "target":"_blank"})
        leaf2 = LEAFNODE("a", "Click Here", props={"href":"https://www.google.com", "target":"_blank"})
        self.assertEqual(leaf1, leaf2)
        


if __name__ == "__main__":
    unittest.main()
