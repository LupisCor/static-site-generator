import unittest
from split_delimiter import(split_nodes_delimiter)
from textnode import TextNode, TextType

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_double_delim(self):
        node = TextNode("This text has **two** words that are **bolded**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("two", TextType.BOLD),
                TextNode(" words that are ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
            ],
            new_nodes
        )

    def test_multiple_delim(self):
        node = TextNode("This text has a **bolded** word and an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This text has a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()