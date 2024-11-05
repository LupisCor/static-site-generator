import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    # def test_eq(self):
        # node = TextNode("This is a text node", TextType.BOLD)
        # node2 = TextNode("This is a text node", TextType.BOLD)
        # self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("a", "test", None, {"href": "https://www.google.com", 
                         "target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()