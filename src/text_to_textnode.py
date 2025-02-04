from split_delimiter import *
from split_functions import *
from textnode import *


def text_to_textnode(text):
    initial_node = TextNode(text, TextType.NORMAL)
    images = split_nodes_image([initial_node])
    links = split_nodes_link(images)
    code = split_nodes_delimiter(links, "`", TextType.CODE)
    bold = split_nodes_delimiter(code, "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "*", TextType.ITALIC)
    return italic

