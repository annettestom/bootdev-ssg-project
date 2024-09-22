import unittest
from textnode import TextNode
from split_nodes import split_nodes_link

class test_split_nodes(unittest.TestCase):
  def test_split_nodes_link(self):
    node1 = [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", "text"), TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", "text")]
    node2 = [TextNode("This text has no links", "text"), TextNode("This text has one link [to boot dev](https://www.boot.dev)", "text")]
    node3 = [TextNode("[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)", "text")]

    self.assertEqual(split_nodes_link(node1), [
      TextNode("This is text with a link ", "text"),
      TextNode("to boot dev", "link", "https://www.boot.dev"),
      TextNode(" and ", "text"),
      TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
      TextNode("This is text with a link ", "text"),
      TextNode("to boot dev", "link", "https://www.boot.dev"),
      TextNode(" and ", "text"),
      TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev")
      ])
    self.assertEqual(split_nodes_link(node2), [
      TextNode("This text has no links", "text"),
      TextNode("This text has one link ", "text"),
      TextNode("to boot dev", "link", "https://www.boot.dev")
      ])
    self.assertEqual(split_nodes_link(node3), [
      TextNode("to boot dev", "link", "https://www.boot.dev"),
      TextNode("to boot dev", "link", "https://www.boot.dev"),
      TextNode("to boot dev", "link", "https://www.boot.dev"),
      TextNode("to boot dev", "link", "https://www.boot.dev")
      ])

  if __name__ == "__main__":
    unittest.main()