import unittest
from textnode import *
from split_delimiter import *

class TestDelimiterFunction(unittest.TestCase):
    def test_1(self):
        result1 = split_nodes_delimiter(
            [TextNode("Hello this `python` is `java` just a test with `go` code in it.", TextType.NORMAL),
             TextNode("This `code` is just another test `more code` with code in it", TextType.NORMAL),
             TextNode("This is `even more code` yet another test with more code in it", TextType.NORMAL)],
             "`", TextType.CODE)
        
        result2 = split_nodes_delimiter(
            [TextNode("Hello this `python` is `java` just a test with `go` code in it.", TextType.NORMAL),
             TextNode("This `code` is just another test `more code` with code in it", TextType.NORMAL),
             TextNode("This is `even more code` yet another test with more code in it", TextType.NORMAL)],
             "`", TextType.CODE)
        self.assertEqual(result1, result2)