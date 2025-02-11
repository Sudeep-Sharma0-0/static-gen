from markdown_to_html import markdown_to_html


def read_markdown():
    with open("src/markdown.md", "r", encoding="utf-8") as file:
        content = file.read()
        return content


with open("src/html.html", "w", encoding="utf-8") as file:
    file.write(f"{markdown_to_html(read_markdown())}")
