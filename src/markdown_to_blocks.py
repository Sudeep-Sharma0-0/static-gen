def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    heading_types = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    block_symbols = ("```", "> ", "* ", "- ")

    sub_blocks = block.splitlines() if "\n" in block else []

    if not block.startswith(block_symbols) and \
            not block.startswith(heading_types) and \
            not block[0].isdigit():
        return "paragraph"

    if len(sub_blocks) < 1:
        if block.startswith(heading_types):
            return "heading"
        if block.startswith("> "):
            return "quote"
        return "paragraph"

    if sub_blocks[0] == "```" and sub_blocks[-1] == "```":
        return "code"

    if block[0].isdigit():
        for sub_block in sub_blocks:
            dot_index = sub_block.find(". ")
            if not dot_index or \
                    not sub_block[0].isdigit() or\
                    not sub_block[dot_index - 1].isdigit():
                return "paragraph"
        return "ordered_list"

    if block.startswith("* ") or block.startswith("- "):
        for sub_block in sub_blocks:
            if not block.startswith("* ") and not block.startswith("- "):
                return "paragraph"
        return "unordered_list"

    if block.startswith("> "):
        for sub_block in sub_blocks:
            if not block.startswith("> "):
                return "paragraph"
        return "quote"
    return "paragraph"
