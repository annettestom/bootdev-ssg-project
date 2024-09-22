from textnode import TextNode

def split_node_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != "text":
      node.text = node.text.replace(delimiter, "")
      new_nodes.append(node)
    else:
      node_list = node.text.split(sep=delimiter)
      if len(node_list) % 2 == 0:
        raise Exception("Invalid Markdown syntax")
      for i in range(len(node_list)):
        if i % 2 != 0:
          new_nodes.append(TextNode(text=node_list[i], text_type=text_type))
        else:
          new_nodes.append(TextNode(text=node_list[i], text_type="text"))
  new_nodes = [n for n in new_nodes if n.text != ""]
  return new_nodes


if __name__ == "__main__":
  node = TextNode("hgfygfytf`code block` word `code block`", "text")
  print(split_node_delimiter([node], "`", "code"))