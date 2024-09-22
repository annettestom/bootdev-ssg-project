import unittest
from block_types import block_to_block_type

class Test_block_types(unittest.TestCase):
  def test_block_to_block_type(self):
    quote_block = ">This is a quote\n>This is a quote\n>This is a quote"
    heading_block = "### This is a heading"
    code_block = "```code block```"
    unordered_list_block = "* unordered list element\n* unordered list element\n* unordered list element"
    unordered_list_block2 = "- unordered list element\n- unordered list element\n- unordered list element"
    ordered_list_block = "1. ordered list element\n2. ordered list element\n3. ordered list element"
    paragraph_block = "This is a paragraph of text"

    self.assertEqual(block_to_block_type(quote_block), "quote")
    self.assertEqual(block_to_block_type(heading_block), "heading")
    self.assertEqual(block_to_block_type(code_block), "code")
    self.assertEqual(block_to_block_type(unordered_list_block), "unordered list")
    self.assertEqual(block_to_block_type(unordered_list_block2), "unordered list")
    self.assertEqual(block_to_block_type(ordered_list_block), "ordered list")
    self.assertEqual(block_to_block_type(paragraph_block), "paragraph")


if __name__ == "__main__":
  unittest.main()