import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_to_html(self):
    node = LeafNode("p", "This is a paragraph of text.")
    node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    node3 = LeafNode("h1", "This is a heading", {
        "href": "https://www.google.com",
        "target": "_blank",
      }
    )
    self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
    self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')
    self.assertEqual(node3.to_html(), '<h1 href="https://www.google.com" target="_blank">This is a heading</h1>')

if __name__ == "__main__":
  unittest.main()

