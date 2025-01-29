import unittest
from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_plain_text(self):
        text = "This is plain text."
        expected = [
            TextNode("This is plain text.", TextType.TEXT)
        ]
        result = split_nodes_delimiter(text)

        self.assertEqual(expected, result)

    def test_bold_text(self):
        text = "This is **bold** text."
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        result = split_nodes_delimiter(text)

        self.assertEqual(expected, result)

    def test_italic_text(self):
        text = "This is *italic* text."
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ]
        result = split_nodes_delimiter(text)

        self.assertEqual(expected, result)

    def test_code_block_text(self):
        text = "This is `code` text."
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.TEXT),
        ]
        result = split_nodes_delimiter(text)

        self.assertEqual(expected, result)

    def test_first_char_delimiter(self):
        text = "*This* is `code` text."
        expected = [
            TextNode("This", TextType.ITALIC),
            TextNode(" is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.TEXT),
        ]
        result = split_nodes_delimiter(text)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
