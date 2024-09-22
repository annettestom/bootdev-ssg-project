import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    node = HTMLNode("a",props={"href": "https://www.google.com", "target": "_blank"}, value=None, children=None)
    node2 = HTMLNode("h1", "This is the heading", children=None, props=None)
    node3 = HTMLNode("p", "This is text", [
      HTMLNode("a",props={"href": "https://www.google.com"}, value=None, children=None),
      HTMLNode(tag=None, value="This is raw text", children=None, props=None)
      ], props=None)
    self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    self.assertEqual(node2.props_to_html(), "")
    self.assertEqual(node3.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()