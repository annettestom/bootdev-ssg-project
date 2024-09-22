from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
  def __init__(self, tag=None, children=None, props=None):
    super().__init__(tag=tag, children=children, props=props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("Tag is required")
    if len(self.children) == 0:
      raise ValueError("Children are required")

    converted_string = f"<{self.tag}{super().props_to_html()}>"
    for child in self.children:
      converted_string += child.to_html()
    converted_string += f"</{self.tag}>"
    return converted_string


if __name__ == "__main__":
  parent_node = ParentNode("p", [LeafNode("b", "Bold text")], {"href": "https://www.google.com"})
  print(parent_node)
  print(parent_node.to_html())

