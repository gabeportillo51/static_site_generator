def markdown_to_blocks(markdown):
    string_list = markdown.split("\n\n")
    new_string_list = []
    for string in string_list:
        new_string = string.strip()
        if len(new_string) == 0:
            continue
        else:
            new_string_list.append(new_string)
    return new_string_list
