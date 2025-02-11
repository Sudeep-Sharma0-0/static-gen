from textnode import TextType, TextTag
from leafnode import LeafNode


def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    if text_type not in TextType:
        raise Exception("Node is not a valid text type!")

    text_tag = f"{TextTag[text_type.value].value}"
    if text_tag == "":
        text_tag = None

    if text_tag == "img":
        image_node = LeafNode(
            tag=text_tag,
            value="",
            props={"src": text_node.url, "alt": text_node.text})
        return image_node

    if text_tag == "a":
        image_node = LeafNode(
            tag=text_tag,
            value=text_node.text,
            props={"href": text_node.url})
        return image_node

    normal_node = LeafNode(
        tag=text_tag,
        value=text_node.text)
    return normal_node
