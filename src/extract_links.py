import re

def extract_markdown_images(text):
  image_tuple_matches = re.findall(r'!\[([^\]]+)\]\(([^)]+)\)', text)
  return image_tuple_matches

def extract_markdown_links(text):
  link_tuple_matches = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)
  return link_tuple_matches

if __name__ == "__main__":
  text_images = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
  text_links1 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
  text_links2 = "[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)"
  print(extract_markdown_images(text_images))
  print(extract_markdown_links(text_links1))
  print(extract_markdown_links(text_links2))


