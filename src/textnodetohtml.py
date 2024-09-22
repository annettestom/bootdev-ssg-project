from leafnode import LeafNode
from textnode import TextNode

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
  if text_node.text_type == "text":
    return LeafNode(None, value = text_node.text)
  elif text_node.text_type == "bold":
    return LeafNode("b", value = text_node.text)
  elif text_node.text_type == "italic":
    return LeafNode("i", value= text_node.text)
  elif text_node.text_type == "code":
    return LeafNode("code", value = text_node.text)
  elif text_node.text_type == "link":
    return LeafNode("a", value = text_node.text, props = {"href": text_node.url})
  elif text_node.text_type == "image":
    return LeafNode("img", value = "", props={"src": text_node.url, "alt": text_node.text})
  else:
    raise Exception(f"{text_node.text_type} is not a permitted text type")

