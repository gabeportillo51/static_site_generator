from extract_functions import extract_markdown_images, extract_markdown_links
from textnode import *

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text) # this is a list of tuples
        if node.text == "":
            pass
        if len(images) == 0:
            new_nodes.append(node)
            pass
        else:
            text = node.text
            for i in range(len(images)):
                sections = text.split(f"![{images[i][0]}]({images[i][1]})")
                image_node = TextNode(images[i][0], TextType.IMAGE, images[i][1])
                if len(extract_markdown_images(sections[1])) != 0:
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                    new_nodes.append(image_node)
                    text = sections[1]
                elif len(extract_markdown_images(sections[1])) == 0 and len(sections[1]) != 0:
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                    new_nodes.append(image_node)
                    new_nodes.append(TextNode(sections[1], TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                    new_nodes.append(image_node)
    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if node.text == "":
            pass
        if len(links) == 0:
            new_nodes.append(node)
            pass
        else:
            text = node.text
            for i in range(len(links)):
                sections = text.split(f"[{links[i][0]}]({links[i][1]})")
                link_node = TextNode(links[i][0], TextType.LINK, links[i][1])
                if len(extract_markdown_links(sections[1])) != 0:
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                    new_nodes.append(link_node)
                    text = sections[1]
                elif len(extract_markdown_links(sections[1])) == 0 and len(sections[1]) != 0:
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                    new_nodes.append(link_node)
                    new_nodes.append(TextNode(sections[1], TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                    new_nodes.append(link_node)
    return new_nodes

