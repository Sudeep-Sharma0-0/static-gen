import unittest
from textnode import TextNode, TextType
from split_links import (
    split_nodes_image, split_nodes_link
)


class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_image_valid(self):
        old_nodes = [
            TextNode(
                "Here is an image: ![alt text](https://example.com/image.jpg)", TextType.TEXT)
        ]
        expected = [
            TextNode("Here is an image: ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE,
                     "https://example.com/image.jpg")
        ]

        result = split_nodes_image(old_nodes)

        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertEqual(r.text, e.text)
            self.assertEqual(r.text_type, e.text_type)
            self.assertEqual(getattr(r, 'additional', None),
                             getattr(e, 'additional', None))

    def test_split_nodes_image_no_images(self):
        old_nodes = [
            TextNode("This text has no images.", TextType.TEXT)
        ]
        result = split_nodes_image(old_nodes)
        self.assertEqual(result, old_nodes)

    def test_split_nodes_link_valid(self):
        old_nodes = [
            TextNode(
                "Here is a link: [example](https://example.com)", TextType.TEXT)
        ]
        expected = [
            TextNode("Here is a link: ", TextType.TEXT),
            TextNode("example", TextType.LINK, "https://example.com")
        ]

        result = split_nodes_link(old_nodes)

        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertEqual(r.text, e.text)
            self.assertEqual(r.text_type, e.text_type)
            self.assertEqual(getattr(r, 'additional', None),
                             getattr(e, 'additional', None))

    def test_split_nodes_link_no_links(self):
        old_nodes = [
            TextNode("This text has no links.", TextType.TEXT)
        ]
        result = split_nodes_link(old_nodes)
        self.assertEqual(result, old_nodes)


if __name__ == "__main__":
    unittest.main()
