class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children if children is not None else []
    self.props = props if props is not None else {}

  def to_html(self):
    raise NotImplementedError

  def props_to_html(self):
    attribute_string = ""
    for k, v in self.props.items():
      attribute_string += f' {k}="{v}"'
    return attribute_string

  def __repr__(self):
    return f"HTMLNode(tag={self.tag},value={self.value},children={self.children},props={self.props})"




if __name__ == "__main__":
  html_node = HTMLNode("p", "The text inside a paragraph", children=None, props={"href": "https://www.google.com"})
  print(html_node)
