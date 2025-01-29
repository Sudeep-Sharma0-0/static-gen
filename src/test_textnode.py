import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("Link text", TextType.LINK, url="http://example.com")
        node2 = TextNode("Link text", TextType.LINK, url="http://example.com")
        self.assertEqual(node, node2)

    def test_neq_different_url(self):
        node = TextNode("Link text", TextType.LINK, url="http://example.com")
        node2 = TextNode("Link text", TextType.LINK,
                         url="http://different.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Code snippet", TextType.CODE)
        self.assertEqual(repr(node), "TextNode(Code snippet, code, None)")

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        node2 = TextNode("", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_neq_empty_text(self):
        node = TextNode("", TextType.TEXT)
        node2 = TextNode("Non-empty", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_neq_different_types_and_urls(self):
        node = TextNode("Image", TextType.IMAGE, url="http://image.com")
        node2 = TextNode("Image", TextType.LINK, url="http://image.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
