import unittest

from textnode import TextNode
from split_delimiter import split_node_delimiter

class Test_split_node_delimiter(unittest.TestCase):
  def test_split_node_delimiter(self):
    node1 = TextNode("This is a text with a `code block` word", "text")
    node2 = TextNode("This is text with a code block at the end `code block`", "text")
    node3 = TextNode("This is a text with **bold text** in the middle", "text")
    node4 = TextNode("**This is just bold text**", "bold")
    node5 = TextNode("This is a text with *italic text* in the middle", "text")
    node6 = TextNode("This is text with *incorrect markdown syntax", "text")

    self.assertEqual(split_node_delimiter([node1, node2],"`", "code"), [
      TextNode("This is a text with a ", "text"),
      TextNode("code block", "code"),
      TextNode(" word", "text"),
      TextNode("This is text with a code block at the end ", "text"),
      TextNode("code block", "code")
      ])
    self.assertEqual(split_node_delimiter([node3, node4], "**", "bold"),[
      TextNode("This is a text with ", "text"),
      TextNode("bold text", "bold"),
      TextNode(" in the middle", "text"),
      TextNode("This is just bold text", "bold")
      ])
    self.assertEqual(split_node_delimiter([node5], "*", "italic"), [
      TextNode("This is a text with ", "text"),
      TextNode("italic text", "italic"),
      TextNode(" in the middle", "text"),
      ])
    with self.assertRaises(Exception):
      split_node_delimiter([node6], "*", "italic")


if __name__ == "__main__":
  unittest.main()