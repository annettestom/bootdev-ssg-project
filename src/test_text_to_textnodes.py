import unittest
from textnode import TextNode
from text_to_textnodes import text_to_textnodes

class Test_text_to_textnodes(unittest.TestCase):
  def test_text_to_textnodes(self):
    text1 = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    text2 = "This text has only one link [link](https://boot.dev) and nothing more."
    text3 = "This text has *italic word* and a **bold word**."
    text4 = "This text has only text"

    self.assertEqual(text_to_textnodes(text1), [
    TextNode("This is ", "text"),
    TextNode("text", "bold"),
    TextNode(" with an ", "text"),
    TextNode("italic", "italic"),
    TextNode(" word and a ", "text"),
    TextNode("code block", "code"),
    TextNode(" and an ", "text"),
    TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", "text"),
    TextNode("link", "link", "https://boot.dev"),
    ])
    self.assertEqual(text_to_textnodes(text2), [
      TextNode("This text has only one link ", "text"),
      TextNode("link", "link", "https://boot.dev"),
      TextNode(" and nothing more.", "text")
    ])
    self.assertEqual(text_to_textnodes(text3), [
      TextNode("This text has ", "text"),
      TextNode("italic word", "italic"),
      TextNode(" and a ", "text"),
      TextNode("bold word", "bold"),
      TextNode(".", "text")
      ])
    self.assertEqual(text_to_textnodes(text4), [
      TextNode("This text has only text", "text")
    ])
if __name__ == "__main__":
  unittest.main()