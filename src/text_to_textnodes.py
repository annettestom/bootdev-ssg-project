from textnode import TextNode
from split_delimiter import split_node_delimiter
from split_nodes import split_nodes_image
from split_nodes import split_nodes_link
from collections import OrderedDict
def text_to_textnodes(text):
  delimiter_dict = OrderedDict([["bold", "**"], ["italic", "*"], ["code", "`"]])
  node_list = [TextNode(text = text, text_type = "text")]
  for text_type, delimiter in delimiter_dict.items():
    node_list = split_node_delimiter(node_list, delimiter=delimiter, text_type=text_type)
  split_node_image_list = split_nodes_image(node_list)
  split_node_links_list = split_nodes_link(split_node_image_list)
  return split_node_links_list

if __name__ == "__main__":
  text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
  print(text_to_textnodes(text))



