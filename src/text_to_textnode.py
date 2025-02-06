from split_delimiter import *
from split_functions import *
from textnode import *


def text_to_textnode(text):
    initial_node = TextNode(text, TextType.NORMAL)
    bold = split_nodes_delimiter([initial_node], "**", TextType.BOLD)
    code = split_nodes_delimiter(bold, "`", TextType.CODE)
    images = split_nodes_image(code)
    links = split_nodes_link(images)
    italic = split_nodes_delimiter(links, "*", TextType.ITALIC)
    return italic
