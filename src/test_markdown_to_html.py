import unittest
from markdown_to_html import (
    markdown_to_html,
    unordered_to_html,
    ordered_to_html,
    quote_to_html,
    code_to_html,
    paragraph_to_html
)


class TestMarkdownToHTML(unittest.TestCase):

    def test_markdown_to_html(self):
        markdown = "# Heading\n\n> Quote\n\n- List item 1\n- List item 2\n\n1. Ordered item 1\n2. Ordered item 2\n\n```\nCode block\n```\n\nParagraph"
        expected_html = "<body><h1>Heading</h1><blockquote>Quote</blockquote><ul><li>List item 1</li><li>List item 2</li></ul><ol><li>Ordered item 1</li><li>Ordered item 2</li></ol><pre><code>\nCode block\n</code></pre><p>Paragraph</p></body>"
        self.assertEqual(markdown_to_html(markdown), expected_html)

    def test_unordered_to_html(self):
        unordered_list = "- Item 1\n- Item 2\n* Item 3"
        expected_html = "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
        self.assertEqual(unordered_to_html(
            unordered_list).to_html(), expected_html)

    def test_ordered_to_html(self):
        ordered_list = "1. Item 1\n2. Item 2\n3. Item 3"
        expected_html = "<ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol>"
        self.assertEqual(ordered_to_html(
            ordered_list).to_html(), expected_html)

    def test_quote_to_html(self):
        quote = "> Quote line 1\n> Quote line 2"
        expected_html = "<blockquote>Quote line 1</blockquote><blockquote>Quote line 2</blockquote>"
        self.assertEqual(quote_to_html(quote)[0].to_html(
        ) + quote_to_html(quote)[1].to_html(), expected_html)

    def test_code_to_html(self):
        code = "```\nCode block\n```"
        expected_html = "<pre><code>\nCode block\n</code></pre>"
        self.assertEqual(code_to_html(code).to_html(), expected_html)

    def test_paragraph_to_html(self):
        paragraph = "This is a paragraph."
        expected_html = "<p>This is a paragraph.</p>"
        self.assertEqual(paragraph_to_html(paragraph).to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
