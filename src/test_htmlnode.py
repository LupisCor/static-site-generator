import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode("a", "test", None, {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_values(self):
        node = HTMLNode("div",
                        "This is a test",
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is a test")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})"
        )
    
    def test_leaf_repr(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.__repr__(), "LeafNode(a, Click me!, {'href': 'https://www.google.com'})")

    def test_leafnode_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>" )

    def test_leafnode_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode(None, "child2")
        child_node3 = LeafNode("div", "child3")
        child_node4 = LeafNode("b", "child4")
        parent_node = ParentNode("p", [child_node1, child_node2, child_node3, child_node4])
        self.assertEqual(parent_node.to_html(), "<p><span>child1</span>child2<div>child3</div><b>child4</b></p>")

    def test_no_tag(self):
        parent_node = ParentNode(None, "child text")
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertEqual("All ParentNodes must have a tag.", str(cm.exception))

    def test_no_child(self):
        parent_node = ParentNode("p", None)
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertEqual("All ParentNodes must have at least one ChildNode", str(cm.exception))

    def test_child_props(self):
        child_node = LeafNode("a", "child value", {"href": "https://www.google.com"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><a href="https://www.google.com">child value</a></div>')
    
    def test_parent_props(self):
        child_node = LeafNode("span", "child value")
        parent_node = ParentNode("a", [child_node], {"href": "https://www.google.com"})
        self.assertEqual(parent_node.to_html(), '<a href="https://www.google.com"><span>child value</span></a>')



if __name__ == "__main__":
    unittest.main()