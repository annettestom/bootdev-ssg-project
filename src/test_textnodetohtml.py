import unittest

from textnode import TextNode
from leafnode import LeafNode
from textnodetohtml import text_node_to_html_node

class Test_text_node_to_html_node(unittest.TestCase):
  def test_text_to_html_node(self):
    node1 = TextNode("This is just raw text", "text")
    node2 = TextNode("This is bold text", "bold")
    node3 = TextNode("This is anchor text", "link", "www.google.com")
    node4 = TextNode("This is an image", "image", "www.image.com")

    self.assertEqual(text_node_to_html_node(node1), LeafNode(None, value="This is just raw text"))
    self.assertEqual(text_node_to_html_node(node2), LeafNode("b", value="This is bold text"))
    self.assertEqual(text_node_to_html_node(node3), LeafNode("a", value="This is anchor text", props={"href": "www.google.com"}))
    self.assertEqual(text_node_to_html_node(node4), LeafNode("img", value="", props={"src": "www.image.com", "alt": "This is an image"}))

if __name__ == "__main__":
  unittest.main()