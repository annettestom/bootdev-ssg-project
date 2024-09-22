from markdown_to_block import markdown_to_blocks
from block_types import block_to_block_type
from leafnode import LeafNode
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnodetohtml import text_node_to_html_node

def markdown_to_html_node(markdown):
  markdown_blocks = markdown_to_blocks(markdown)
  node_list = []
  for block in markdown_blocks:
    block_type = block_to_block_type(block)
    block_node = None
    html_content = ""
    if block_type == "quote":
      list_of_textnodes = text_to_textnodes(block[2:])
      for node in list_of_textnodes:
        html_content += text_node_to_html_node(node).to_html()
      block_node = LeafNode("blockquote" ,html_content, None)

    elif block_type == "unordered list":
      block_children: list[LeafNode] = []
      for element in block.split("\n"):
        html_content = ""
        element_textnode_list = text_to_textnodes(element[2:])
        for node in element_textnode_list:
          html_content += text_node_to_html_node(node).to_html()
        block_children.append(LeafNode("li", html_content, None))
      block_node = ParentNode("ul", block_children, None)

    elif block_type == "ordered list":
      block_children: list[LeafNode] = []
      for element in block.split("\n"):
        html_content = ""
        element = element.lstrip('0123456789')[2:]
        element_textnode_list = text_to_textnodes(element)
        for node in element_textnode_list:
          html_content += text_node_to_html_node(node).to_html()
        block_children.append(LeafNode("li", html_content, None))
      block_node = ParentNode("ol", block_children, None)

    elif block_type == "code":
      block_to_textnodes = text_to_textnodes(block)
      for node in block_to_textnodes:
        html_content += text_node_to_html_node(node).to_html()
      block_children = [LeafNode("code", html_content, None)]
      block_node = ParentNode("pre", block_children , None)

    elif block_type == "heading":
      count = 0
      while block.startswith("#"):
        count += 1
        block = block[1:]
      textnode_list = text_to_textnodes(block[1:])
      for node in textnode_list:
        html_content += text_node_to_html_node(node).to_html()
      block_node = LeafNode(f"h{count}", html_content, None)

    else:
      textnode_list = text_to_textnodes(block)
      for node in textnode_list:
        html_content += text_node_to_html_node(node).to_html()
      block_node = LeafNode("p", html_content, None)
    node_list.append(block_node)
  return ParentNode(tag="div", children=node_list, props=None)


if __name__ == "__main__":
  markdown_example = ">This is a quote\n>This is a quote\n>This is a quote\n\n### This is a heading\n\n```code block```\n\n* unordered list element\n* unordered list element\n* unordered list element\n\n1. ordered list element\n2. ordered list element\n3. ordered list element\n\nThis is a paragraph of text"
  print(markdown_to_html_node(markdown_example))