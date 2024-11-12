
from textnode import TextNode, TextType

node = TextNode("this is text with a `code` word", TextType.TEXT)
node2 = TextNode("this is text with a **bold** word", TextType.TEXT)
node3 = TextNode("this is text with a *italic* word", TextType.TEXT)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_nodes = []
        split_list = node.text.split(delimiter)

        if len(split_list) == 2:
            raise Exception("No closing delimiter")
        
        if len(split_list) == 3:
            split_nodes.append(TextNode(split_list[0], TextType.TEXT))
            split_nodes.append(TextNode(split_list[1], text_type))
            split_nodes.append(TextNode(split_list[2], TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes


new_nodes = split_nodes_delimiter([node, node2, node3], "`", TextType.CODE)
#new_nodes2 = split_nodes_delimiter([node, node2, node3], "*", TextType.CODE)
#new_nodes3 = split_nodes_delimiter([node, node2, node3], "**", TextType.CODE)
