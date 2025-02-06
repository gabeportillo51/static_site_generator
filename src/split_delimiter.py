from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type.value != "normal":
            new_nodes.append(node)
            continue
        elif node.text.count(delimiter) % 2 != 0:
            raise Exception("invalid markdown syntax")
        else:
            split_node = node.text.split(delimiter)
            for i in range(len(split_node)):
                if split_node[i] == "":
                    continue
                if i % 2 == 0 and len(split_node[i]) != 0:
                    new_nodes.append(TextNode(split_node[i], TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(split_node[i], text_type))                                
    return new_nodes
