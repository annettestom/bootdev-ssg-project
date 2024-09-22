import unittest
from markdown_to_html import markdown_to_html_node
from leafnode import LeafNode
from parentnode import ParentNode
class Test_markdown_to_html(unittest.TestCase):
  def test_markdown_to_html_node(self):
    markdown1 ="###### This is a heading\n\n```This is a code block```\n\n\nThis is a paragraph of text"
    markdown2 = "\n1. ordered list element\n2. ordered list element\n3. ordered list element\n\n>This is a quote\n>This is a quote\n>This is a quote"

    self.assertEqual(markdown_to_html_node(markdown1).to_html(), ParentNode(tag="div", children=[
      LeafNode(tag="h6", value="This is a heading", props={}),
      ParentNode(tag="pre", children=[
        LeafNode(tag="code", value= "```This is a code block```", props=None )
        ]),
      LeafNode(tag="p", value="This is a paragraph of text", props=None)
      ]).to_html())

    self.assertEqual(markdown_to_html_node(markdown2).to_html(), ParentNode(tag="div", children=[
      ParentNode(tag="ol", children=[
        LeafNode(tag="li",value="1. ordered list element",props=None),
        LeafNode(tag="li", value="2. ordered list element",props=None),
        LeafNode(tag="li",value="3. ordered list element",props=None)
        ],props=None),
      LeafNode(tag="blockquote", value= ">This is a quote\n>This is a quote\n>This is a quote", props=None)
      ]).to_html())


if __name__ == "__main__":
  unittest.main()