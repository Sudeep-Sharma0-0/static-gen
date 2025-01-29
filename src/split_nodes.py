import re
from enum import Enum
from textnode import TextNode
from textnode import TextType


class MarkdownDelimiter(Enum):
    BOLD = "**"
    ITALIC = "*"
    CODE_BLOCK = "`"


def split_nodes_delimiter(text):
    enum_pattern = "|".join(
        f"({re.escape(member.value)})" for member in MarkdownDelimiter)
    pattern = re.compile(enum_pattern)

    split_text = pattern.split(text)
    cleaned_split = [part for part in split_text if part]

    dlmtrs = [i.value for i in MarkdownDelimiter]
    nodes = []
    index = 0
    prev_dlmtr = None
    dlmtr_open = False

    while len(cleaned_split) >= 1:
        if index == len(cleaned_split) - 1:
            prev_dlmtr = cleaned_split[index] if dlmtr_open else None
            nodes.append(nodes_creator(cleaned_split[0], prev_dlmtr))
            del cleaned_split[0]
        elif cleaned_split[index] in dlmtrs:
            if index == 0:
                prev_dlmtr = cleaned_split[index] if dlmtr_open else None
                dlmtr_open = not dlmtr_open
                del cleaned_split[0]
                continue

            text = "".join([cleaned_split[i] for i in range(0, index)])
            prev_dlmtr = cleaned_split[index] if dlmtr_open else None
            nodes.append(nodes_creator(text, prev_dlmtr))

            del cleaned_split[0:index]
            del cleaned_split[0]
            dlmtr_open = not dlmtr_open
            index = 0

        else:
            index += 1

    return nodes


def nodes_creator(text, delimiter):
    if delimiter is None:
        return TextNode(text, TextType.TEXT)
    elif delimiter == MarkdownDelimiter.BOLD.value:
        return TextNode(text, TextType.BOLD)
    elif delimiter == MarkdownDelimiter.ITALIC.value:
        return TextNode(text, TextType.ITALIC)
    elif delimiter == MarkdownDelimiter.CODE_BLOCK.value:
        return TextNode(text, TextType.CODE)
    else:
        raise ValueError("Not a valid delimiter!")
