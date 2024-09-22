import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
  def test_to_html(self):
    node1 = ParentNode(None, [LeafNode("b", "Bold text")], {"href": "https://www.google.com"})
    node2 = ParentNode("p", None, {"href": "https://www.google.com"})
    node3 = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode("i", "italic text")], {"href": "https://www.google.com"})
    node4 = ParentNode("p", [ParentNode("p", [LeafNode("b", "Bold text")], {"href": "https://www.google.com"})], {"href": "https://www.boot.dev"})

    with self.assertRaises(ValueError):
      node1.to_html()

    with self.assertRaises(ValueError):
      node2.to_html()

    self.assertEqual(node3.to_html(), '<p href="https://www.google.com"><b>Bold text</b><i>italic text</i></p>')
    self.assertEqual(node4.to_html(), '<p href="https://www.boot.dev"><p href="https://www.google.com"><b>Bold text</b></p></p>')

if __name__ == "__main__":
  unittest.main()