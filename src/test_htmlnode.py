import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_create_empty_node(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_create_node_with_tag(self):
        node = HTMLNode(tag="div")
        self.assertEqual(node.tag, "div")
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_create_node_with_value(self):
        node = HTMLNode(value="Hello, World!")
        self.assertIsNone(node.tag)
        self.assertEqual(node.value, "Hello, World!")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_create_node_with_children(self):
        child_node = HTMLNode(tag="span", value="child")
        node = HTMLNode(children=[child_node])
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [child_node])
        self.assertIsNone(node.props)

    def test_create_node_with_props(self):
        props = {"class": "container", "id": "main"}
        node = HTMLNode(props=props)
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertEqual(node.props, props)

    def test_props_to_html(self):
        props = {"class": "container", "id": "main"}
        node = HTMLNode(props=props)
        expected_html = 'class="container" id="main"'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_repr(self):
        child_node = HTMLNode(tag="span", value="child")
        props = {"class": "container", "id": "main"}
        node = HTMLNode(tag="div", value="Hello, World!",
                        children=[child_node], props=props)
        expected_repr = "HTMLNode(tag: div, value: Hello, World!, children: [HTMLNode(tag: span, value: child, children: None, props: None)], props: {'class': 'container', 'id': 'main'})"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
