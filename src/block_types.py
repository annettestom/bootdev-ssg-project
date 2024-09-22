import re
def block_to_block_type(block):
  heading_match = re.search(r'^(#{1,6})\s+(.*)$', block)
  code_match = re.search(r'```[\s\S]*?```', block)
  if all(row[0] == ">" for row in block.split("\n")):
    return "quote"
  if heading_match:
    return "heading"
  if code_match:
    return "code"
  if all((row[:2] == "* ") or (row[:2] == "- ") for row in block.split("\n")):
    return "unordered list"
  if all(row.startswith(f"{index+1}. ") for index, row in enumerate(block.split("\n"))):
    return "ordered list"
  else:
    return "paragraph"

if __name__ == "__main__":
  block = ">this is a quote\n>this is also a quote\n>this is a third quote"
  print(block_to_block_type(block))



