import re


def extract_markdown_images(text):
    img_pattern = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
    matches = img_pattern.findall(text)
    images = [(alt, url) for alt, url in matches]
    return images


def extract_markdown_links(text):
    link_pattern = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
    matches = link_pattern.findall(text)
    links = [(alt, url) for alt, url in matches]
    return links
