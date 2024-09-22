import os
from generate_page import generate_page
def generate_pages_recursive(dir_content_root, dir_path_content, template_path, dest_dir_path):
  try:
    for item in os.listdir(dir_path_content):
      item_path = os.path.join(dir_path_content, item)
      if os.path.isfile(item_path):
        relative_path = os.path.relpath(item_path, dir_content_root)
        dest_path = os.path.join(dest_dir_path, relative_path)
        dir_name = os.path.dirname(dest_path)
        if not os.path.exists(dir_name):
          os.makedirs(dir_name)
        pre, ext = os.path.splitext(dest_path)
        new_dest_path = pre + ".html"
        generate_page(item_path, template_path, new_dest_path)
      if os.path.isdir(item_path):
        generate_pages_recursive(dir_content_root, item_path, template_path, dest_dir_path)
    return True
  except Exception as e:
    print(f"An error occured while generating pages: {e}")
    return False