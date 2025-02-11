import unittest
from extract_links import extract_markdown_images, extract_markdown_links


class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = (
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) "
            "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)."
        )
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(extract_markdown_images(text), expected)

        text_no_images = "This text has no images."
        self.assertEqual(extract_markdown_images(text_no_images), [])

        text_missing_alt = "![](https://example.com/image.png)"
        expected_missing_alt = [("", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(
            text_missing_alt), expected_missing_alt)

        text_invalid = "This is an invalid image tag ![example](invalid"
        self.assertEqual(extract_markdown_images(text_invalid), [])

    def test_extract_markdown_links(self):
        text = (
            "This is text with a link [to boot dev](https://www.boot.dev) "
            "and [to youtube](https://www.youtube.com/@bootdotdev)."
        )
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(extract_markdown_links(text), expected)

        text_no_links = "This text has no links."
        self.assertEqual(extract_markdown_links(text_no_links), [])

        text_missing_alt = "[](https://example.com/page)"
        expected_missing_alt = [("", "https://example.com/page")]
        self.assertEqual(extract_markdown_links(
            text_missing_alt), expected_missing_alt)

        text_invalid = "This is an invalid link tag [example](invalid"
        self.assertEqual(extract_markdown_links(text_invalid), [])

        text_special_characters = (
            "[Check this out!](https://example.com) and [Hello, World](https://test.com)"
        )
        expected_special = [
            ("Check this out!", "https://example.com"),
            ("Hello, World", "https://test.com"),
        ]
        self.assertEqual(extract_markdown_links(
            text_special_characters), expected_special)


if __name__ == "__main__":
    unittest.main()
