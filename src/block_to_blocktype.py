import re

def block_to_blocktype(block):
    lines = block.split("\n")
    is_heading = re.findall(r"^\#{1,6}\ .+", block)
    if len(is_heading) > 0:
        return "heading"
    is_code = re.findall(r"\`{3}", block)
    if len(is_code) == 2:
        return "code"
    count_arrows = re.findall(r"\>", block)
    if len(count_arrows) == len(block.split("\n")):
        return "quote"
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return "paragraph"
        return "unordered list"
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("* "):
                return "paragraph"
        return "unordered list"
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered list"
    else:
        return "paragraph"
    