import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_valid_parent_node(self):
        child1 = LeafNode(tag="p", value="This is a paragraph.")
        child2 = LeafNode(tag="a", value="Click me!", props={
                          "href": "https://www.example.com"})
        parent = ParentNode(tag="div", children=[child1, child2])
        expected_html = '<div><p>This is a paragraph.</p><a href="https://www.example.com">Click me!</a></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_no_tag(self):
        child = LeafNode(tag="p", value="This is a paragraph.")
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[child]).to_html()

    def test_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=[]).to_html()

    def test_nested_parent_nodes(self):
        grandchild = LeafNode(tag="span", value="Nested content")
        child = ParentNode(tag="div", children=[grandchild])
        parent = ParentNode(tag="section", children=[child])
        expected_html = '<section><div><span>Nested content</span></div></section>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_with_props(self):
        child = LeafNode(tag="p", value="This is a paragraph.")
        parent = ParentNode(tag="div", children=[child], props={
                            "class": "container"})
        expected_html = '<div class="container"><p>This is a paragraph.</p></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_multiple_children(self):
        child1 = LeafNode(tag="p", value="First paragraph.")
        child2 = LeafNode(tag="p", value="Second paragraph.")
        child3 = LeafNode(tag="p", value="Third paragraph.")
        parent = ParentNode(tag="div", children=[child1, child2, child3])
        expected_html = '<div><p>First paragraph.</p><p>Second paragraph.</p><p>Third paragraph.</p></div>'
        self.assertEqual(parent.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
