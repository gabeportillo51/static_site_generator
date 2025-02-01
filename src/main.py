from textnode import *
from htmlnode import *

def main():
    print(TextNode("This is a text node", TextType.BOLD, "https://www.bootdev.com"))
    node = HTMLNODE(props={"href": "https://www.google.com", "target": "_blank"})
    print(node.props_to_html())
    
main()