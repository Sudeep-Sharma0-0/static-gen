from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from markdown_to_html import markdown_to_html
import os


def generate_page(src, template, dest):
    print(f"Generating page from {src} to {dest} using {template}...")

    if os.path.isfile(src):
        markdown_file = open(src)
        markdown_text = markdown_file.read()
        markdown_file.close()

        title = get_title(markdown_text)
        html_content = markdown_to_html(markdown_text)

        template_file = open(template)
        template_text = template_file.read()
        template_file.close()

        html_file_text = template_text.replace("{{ Title }}", title)
        html_file_text = html_file_text.replace("{{ Content }}", html_content)

        dest_file = open(f"{dest.replace(".md", ".html")}", "w")
        dest_file.write(html_file_text)

    if os.path.isdir(src):
        files = os.listdir(src)
        if src != "content":
            os.mkdir(dest)
        for file in files:
            generate_page(f"{src}/{file}", template, f"{dest}/{file}")


def get_title(markdown):
    blocks = markdown_to_blocks(markdown)
    title = ""

    for block in blocks:
        if block_to_block_type(block) == "heading":
            title += block[2:] if block.startswith("# ") else ""

    if title.strip() == "":
        raise Exception("No title found in page!")
    return title
