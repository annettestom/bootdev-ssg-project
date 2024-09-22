from markdown_to_block import markdown_to_blocks
def extract_title(markdown):
  markdown_block = markdown_to_blocks(markdown)
  try:
    for line in markdown_block:
      if line.startswith("#"):
        return line.strip("# ")
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  markdown = "  # This is a heading\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n * This is the first list item in a list block\n* This is a list item\n* This is another list item"
  print(extract_title(markdown))


