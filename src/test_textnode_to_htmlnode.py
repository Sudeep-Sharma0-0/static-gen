import unittest
from textnode import TextType, TextTag, TextNode
from parentnode import ParentNode
from leafnode import LeafNode
from textnode_to_htmlnode import text_node_to_html_node


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_plain_text_node(self):
        text_node = TextNode("Hello, world!", TextType.TEXT)
        result = text_node_to_html_node(text_node)
        expected = LeafNode(
            tag=None, value="Hello, world!")
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)

    def test_image_node(self):
        text_node = TextNode("Image description", TextType.IMAGE,
                             url="http://example.com/image.png")
        result = text_node_to_html_node(text_node)
        expected = LeafNode(tag="img", value="Image description", props={
                            "href": "http://example.com/image.png"})
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)
        self.assertEqual(result.props, expected.props)

    def test_link_node(self):
        text_node = TextNode("Click me", TextType.LINK,
                             url="http://example.com")
        result = text_node_to_html_node(text_node)
        expected = LeafNode(
            tag="a",
            props={"href": "http://example.com"},
            value="Click me"
        )
        self.assertEqual(result.tag, expected.tag)

    def test_parent_link(self):
        text_node = TextNode("Click me", TextType.BOLD,
                             url="http://example.com")
        result = text_node_to_html_node(text_node)
        expected = ParentNode(
            tag="a",
            children=[LeafNode(tag="b", value="Click me")],
            props={"href": "http://example.com"}
        )
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(len(result.children), len(expected.children))
        self.assertEqual(result.children[0].tag, expected.children[0].tag)
        self.assertEqual(result.children[0].value, expected.children[0].value)
        self.assertEqual(result.children[0].props, expected.children[0].props)

    def test_invalid_text_type(self):
        text_node = TextNode("Invalid node", "INVALID_TYPE")
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception),
                         "Node is not a valid text type!")

    def test_unsupported_text_type(self):
        class FakeTextType:
            pass

        text_node = TextNode("Unsupported node", FakeTextType)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception),
                         "Node is not a valid text type!")


if __name__ == "__main__":
    unittest.main()
