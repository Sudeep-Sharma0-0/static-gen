from enum import Enum
from split_nodes import split_nodes_delimiter
from split_links import (
    split_nodes_image,
    split_nodes_link
)
from textnode import TextType, TextNode
from textnode_to_htmlnode import text_node_to_html_node


class MarkdownDelimiters(Enum):
    BOLD = "**"
    ITALIC = "*"
    STRIKE_THROUGH = "~~"
    CODE = "`"


def text_to_nodes(text):
    nodes = [TextNode(text=text, text_type=TextType.TEXT)]
    for dlmtr in MarkdownDelimiters:
        if dlmtr.value not in text:
            continue
        nodes = split_nodes_delimiter(
            nodes, dlmtr.value, TextType[dlmtr.name])
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    converted_nodes = list(map(lambda x: text_node_to_html_node(x), nodes))
    return converted_nodes
