from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from split_delimiter import *
from text_to_textnode import *

def main():
    print(TextNode("This is a text node", TextType.BOLD, "https://www.bootdev.com"))
    node = HTMLNODE(props={"href": "https://www.google.com", "target": "_blank"})
    print(node.props_to_html())
    leaf = LEAFNODE("b", "Click Here", props={"href":"https://www.google.com", "target":"_blank"})
    print(leaf.to_html())
    parent = PARENTNODE("p", [LEAFNODE("b", "Bold text"), LEAFNODE(None, "Normal text"), LEAFNODE("i", "italic text"), LEAFNODE(None, "Normal text")], props={"href": "https://www.google.com", "target": "_blank"})
    print(parent.to_html())
    print("Converting text node to leaf node using the .text_node_to_html_node() method:")
    print("This is the textnode:")
    text_node = TextNode("This is a fucking text node", TextType.LINK, "www.youtube.com")
    print(text_node)
    print("This is the leaf node version of the above text node:")
    leaf_text_node = text_node.text_node_to_html_node()
    print(leaf_text_node.to_html())
    print("\n")
    print("\n")
    print("\n")
    print("Testing split delimiter function:")
    node = TextNode("This is text with a `code` block.", TextType.NORMAL)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)
    print("\n")
    print("\n")
    print("\n")
    print(text_to_textnode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))




main()