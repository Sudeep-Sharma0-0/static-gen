import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_valid_input(self):
        old_nodes = [TextNode("This is **bold** text.", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", text_type),
            TextNode(" text.", TextType.TEXT)
        ]

        result = split_nodes_delimiter(old_nodes, delimiter, text_type)

        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertEqual(r.text, e.text)
            self.assertEqual(r.text_type, e.text_type)

    def test_split_nodes_no_delimiters(self):
        old_nodes = [TextNode("This has no formatting.", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD

        expected = old_nodes

        result = split_nodes_delimiter(old_nodes, delimiter, text_type)

        self.assertEqual(result, expected)

    def test_split_nodes_invalid_input(self):
        old_nodes = [TextNode("This is **invalid markdown.", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD

        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, delimiter, text_type)


if __name__ == "__main__":
    unittest.main()
