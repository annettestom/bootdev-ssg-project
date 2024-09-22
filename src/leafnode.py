from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, props=None):
      super().__init__(tag=tag, value=value, props=props)

  def to_html(self):
    if self.value is None:
      raise ValueError
    if self.tag is None:
      return f"{self.value}"
    return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"

  def __repr__(self):
    return f"LeafNode(tag={self.tag},value={self.value},props={self.props})"

  def __eq__(self, other):
    return isinstance(other, LeafNode) and self.tag == other.tag and self.value == other.value and self.props == other.props

if __name__ == "__main__":
  leaf_node = LeafNode("p", "This is a paragraph of text.", {"href": "https://www.google.com"})
  print(leaf_node)
  print(leaf_node.to_html())