
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type): #list, str, TextType
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        split_list = old_node.text.split(delimiter)

        if len(split_list) % 2 == 0:
            raise ValueError("No closing delimiter")
        
        for i in range(len(split_list)):
            if split_list[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_list[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(split_list[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes