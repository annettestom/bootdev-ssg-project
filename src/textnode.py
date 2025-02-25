class TextNode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other) -> bool:
    return self.text == other.text and self.text_type == other.text_type and self.url == other.url

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"

def main():
  dummy_object = TextNode("This is a text node", "bold", "https://www.boot.dev")
  print(dummy_object)

if __name__ == "__main__":
  main()