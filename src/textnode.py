from enum import Enum


class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    STRIKE_THROUGH = "strike"


class TextTag(Enum):
    normal = ""
    bold = "b"
    italic = "i"
    code = "code"
    link = "a"
    image = "img"
    strike = "strike"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        equality = self.text == other_node.text \
            and self.text_type == other_node.text_type \
            and self.url == other_node.url

        return equality

    def __repr__(self):
        reprsntatn = f"TextNode({self.text}, {
            self.text_type.value}, {self.url})"
        return reprsntatn
