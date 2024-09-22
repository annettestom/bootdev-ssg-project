from markdown_to_html import markdown_to_html_node
from extract_markdown_title import extract_title
import os
def generate_page(from_path, template_path, dest_path):
  try:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as file:
      from_content = file.read()
    with open(template_path, 'r') as file2:
      template_content = file2.read()

    from_html_string = (markdown_to_html_node(from_content)).to_html()
    page_title = extract_title(from_content)
    template_content = template_content.replace("{{ Title }}", page_title)
    new_content = template_content.replace("{{ Content }}", from_html_string)

    dir_name = os.path.dirname(dest_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    with open(dest_path, 'w') as file3:
      file3.write(new_content)
    return True

  except Exception as e:
    print(f"An error occured: {e}")
    return False


