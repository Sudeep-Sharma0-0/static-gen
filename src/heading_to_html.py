from parentnode import ParentNode
from text_to_nodes import text_to_nodes


def heading_to_html(heading):
    if heading.startswith("# "):
        index = heading.find("# ")
        heading_text = heading[:index] + heading[index + len("# "):]
        return ParentNode("h1", text_to_nodes(heading_text))
    if heading.startswith("## "):
        index = heading.find("## ")
        heading_text = heading[:index] + heading[index + len("## "):]
        return ParentNode("h2", text_to_nodes(heading_text))
    if heading.startswith("### "):
        index = heading.find("### ")
        heading_text = heading[:index] + heading[index + len("### "):]
        return ParentNode("h3", text_to_nodes(heading_text))
    if heading.startswith("#### "):
        index = heading.find("#### ")
        heading_text = heading[:index] + heading[index + len("#### "):]
        return ParentNode("h4", text_to_nodes(heading_text))
    if heading.startswith("##### "):
        index = heading.find("##### ")
        heading_text = heading[:index] + heading[index + len("##### "):]
        return ParentNode("h5", text_to_nodes(heading_text))
    if heading.startswith("###### "):
        index = heading.find("###### ")
        heading_text = heading[:index] + heading[index + len("###### "):]
        return ParentNode("h6", text_to_nodes(heading_text))
