import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_no_tag(self):
        node = LeafNode(value="Just a string")
        self.assertEqual(node.to_html(), "Just a string")

    def test_with_tag(self):
        node = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_with_props(self):
        node = LeafNode(tag="a", value="Click me!", props={
                        "href": "https://www.example.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.example.com">Click me!</a>')

    def test_no_value(self):
        node = LeafNode(tag="div")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_empty_value(self):
        node = LeafNode(tag="span", value="")
        self.assertEqual(node.to_html(), "<span></span>")

    def test_multiple_props(self):
        node = LeafNode(tag="img", value="", props={
                        "src": "image.png", "alt": "An image"})
        self.assertEqual(
            node.to_html(), '<img src="image.png" alt="An image"></img>')


if __name__ == "__main__":
    unittest.main()
