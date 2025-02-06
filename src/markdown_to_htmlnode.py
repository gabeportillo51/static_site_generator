from markdown_to_blocks import *
from block_to_blocktype import *
from textnode import *
from htmlnode import *
from text_to_textnode import *
import re
from parentnode import *

def text_node_conversion(text):
    text_nodes = text_to_textnode(text)
    new = []
    for text_node in text_nodes:
        new.append(text_node.text_node_to_html_node())
    return new

def list_tags(text):
    lines = text.split("\n")
    list_nodes = []
    for line in lines:
        list_nodes.append(PARENTNODE("li", text_node_conversion(line.strip())))
    return list_nodes

def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_blocktype(block)
        if block_type == "heading":
            head_num = re.findall(r"\#{1,6}", block)[0].count("#")
            html_nodes.append(PARENTNODE(f"h{head_num}", text_node_conversion(block.replace("#", "").strip())))
        elif block_type == "code":
            html_nodes.append(PARENTNODE("pre", [PARENTNODE("code", text_node_conversion(block.replace("```", "").strip()))]))
        elif block_type == "quote":
            html_nodes.append(PARENTNODE("blockquote", text_node_conversion(block.replace(">", "").strip())))
        elif block_type == "unordered list":
            new_block_list = []
            lines = block.split("\n")
            for line in lines:
                new_block_list.append(line[2:])
            new_block = "\n".join(new_block_list)
            html_nodes.append(PARENTNODE("ul", list_tags(new_block.strip())))
        elif block_type == "ordered list":
            no_nums = block.split("\n")
            new = []
            for line in no_nums:
                new.append(line[3:])
            no_nums_2 = "\n".join(new)
            html_nodes.append(PARENTNODE("ol", list_tags(no_nums_2.strip())))
        elif block_type == "paragraph":
            html_nodes.append(PARENTNODE("p", text_node_conversion(block.strip())))
    return PARENTNODE("div", html_nodes)
