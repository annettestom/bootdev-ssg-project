import unittest
from markdown_to_block import markdown_to_blocks

class Test_markdown_to_block(unittest.TestCase):
  def test_markdown_to_blocks(self):
    text1 = "\n\n\n\n# This is the heading\n\nThis text has **bold words** and *italic words*\n\n* This is a list item\n* This is a list item"
    text2 = "  # This is a heading\n\n This is a paragraph of text \n\n\t * This is a list item\n* and this also "
    text3 = "# This is a heading\n\nThis is text\n\n* and this is first list item\n* this is a second list item"

    self.assertEqual(markdown_to_blocks(text1), [
      "# This is the heading",
      "This text has **bold words** and *italic words*",
      "* This is a list item\n* This is a list item"
      ])
    self.assertEqual(markdown_to_blocks(text2), [
      "# This is a heading",
      "This is a paragraph of text",
      "* This is a list item\n* and this also"
    ])
    self.assertEqual(markdown_to_blocks(text3), [
      "# This is a heading",
      "This is text",
      "* and this is first list item\n* this is a second list item"
      ])

if __name__ == "__main__":
  unittest.main()

