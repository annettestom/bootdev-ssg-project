import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a different text node", "bold", "https://www.boot.dev")
        self.assertNotEqual(node1, node2)
        node1_2 = TextNode("This is some text", "normal" , "https://www.boot.dev")
        node2_2 = TextNode("This is some text", "normal")
        self.assertNotEqual(node1_2, node2_2)


if __name__ == "__main__":
    unittest.main()