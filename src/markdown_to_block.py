def markdown_to_blocks(markdown) -> list[str]:
  string_list = markdown.split("\n\n")
  new_string_list = []
  for sone in string_list:
    new_sone = sone.strip(" \n\t")
    if len(new_sone) != 0:
      new_string_list.append(new_sone)
  return new_string_list

if __name__ == "__main__":
  text = "  # This is a heading\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n * This is the first list item in a list block\n* This is a list item\n* This is another list item"
  print(markdown_to_blocks(text))
