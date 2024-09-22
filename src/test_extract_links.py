import unittest

from extract_links import extract_markdown_images
from extract_links import extract_markdown_links

class Test_ectract_links(unittest.TestCase):
  def test_extract_markdown_images(self):
    text1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    text2 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
    text3 = "This text has no images or links"

    self.assertEqual(extract_markdown_images(text1), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
    self.assertEqual(extract_markdown_images(text2), [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])
    self.assertEqual(extract_markdown_images(text3), [])

  def test_extract_markdown_links(self):
    text1 = "This text has no links"
    text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    text3 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and [to boot dev](https://www.boot.dev)"

    self.assertEqual(extract_markdown_links(text1), [])
    self.assertEqual(extract_markdown_links(text2), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
    self.assertEqual(extract_markdown_links(text3), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev"), ("to boot dev", "https://www.boot.dev")])

if __name__ == "__main__":
  unittest.main()
