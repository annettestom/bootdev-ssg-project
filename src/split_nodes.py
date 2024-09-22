from extract_links import extract_markdown_links
from extract_links import extract_markdown_images
from textnode import TextNode

def split_nodes_link(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != "text":
      new_nodes.append(node)
      continue
    link_list = extract_markdown_links(node.text)
    # print(link_list)
    node_text_links_replaced = node.text
    for x in link_list:
      node_text_links_replaced = node_text_links_replaced.replace(f"[{x[0]}]({x[1]})", "**?")
    node_text_list = node_text_links_replaced.split("**?")
    for i in range(len(node_text_list)):
      new_nodes.append(TextNode(text = node_text_list[i], text_type = "text"))
      if i < len(link_list):
        new_nodes.append(TextNode(text = f"{link_list[i][0]}", text_type = "link", url = f"{link_list[i][1]}"))
    new_nodes = [n for n in new_nodes if n.text != ""]
  return new_nodes

def split_nodes_image(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != "text":
      new_nodes.append(node)
      continue
    image_list = extract_markdown_images(node.text)
    node_text_images_replaced = node.text
    for x in image_list:
      node_text_images_replaced = node_text_images_replaced.replace(f"![{x[0]}]({x[1]})", "**?")
    node_text_list = node_text_images_replaced.split("**?")
    for i in range(len(node_text_list)):
      new_nodes.append(TextNode(text = node_text_list[i], text_type = "text"))
      if i < (len(image_list)):
        new_nodes.append(TextNode(text = f"{image_list[i][0]}", text_type = "image", url = f"{image_list[i][1]}"))
    new_nodes = [n for n in new_nodes if n.text != ""]
  return new_nodes

if __name__ == "__main__":
  node_list = [TextNode("[to boot dev](https://www.boot.dev) This is text with a link [to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev)", "text")]
  node_list2 = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", "text")]
  node_list3 = [TextNode("[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)", "text")]
  print(split_nodes_link(node_list3))
  split_nodes_image(node_list2)