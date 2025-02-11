from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from parentnode import ParentNode
from textnode import TextNode, TextType
from text_to_nodes import text_to_nodes
from heading_to_html import heading_to_html
from textnode_to_htmlnode import text_node_to_html_node


def markdown_to_html(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    html_children = []
    for block in markdown_blocks:
        block_type = block_to_block_type(block)

        if block_type == "heading":
            html_children.append(heading_to_html(block))
        if block_type == "quote":
            html_children.extend(quote_to_html(block))
        if block_type == "unordered_list":
            html_children.append(unordered_to_html(block))
        if block_type == "ordered_list":
            html_children.append(ordered_to_html(block))
        if block_type == "code":
            html_children.append(code_to_html(block))
        if block_type == "paragraph":
            html_children.append(paragraph_to_html(block))

    html_node = ParentNode("div", children=html_children)
    return html_node.to_html()


def unordered_to_html(list):
    items = list.splitlines()
    children = []
    for item in items:
        index = item.find("- ") if "- " in item else item.find("* ")
        text = item[index+2:]
        children.append(ParentNode("li", text_to_nodes(text)))
    node = ParentNode("ul", children)
    return node


def ordered_to_html(list):
    items = list.splitlines()
    children = []
    for item in items:
        index = item.find(". ")
        text = item[index+2:]
        children.append(ParentNode("li", text_to_nodes(text)))
    node = ParentNode("ol", children)
    return node


def quote_to_html(quote):
    items = quote.splitlines()
    nodes = []
    for item in items:
        index = item.find("> ")
        text = item[index+2:]
        nodes.append(ParentNode("blockquote", text_to_nodes(text)))
    return nodes


def code_to_html(code):
    return ParentNode(
        "pre",
        [text_node_to_html_node(
            TextNode(code.replace("```", ""), TextType.CODE))]
    )


def paragraph_to_html(paragraph):
    return ParentNode("p", text_to_nodes(paragraph))
