import shutil
import os
def copy_to_destination(source, destination):
  try:
    if not os.path.exists(destination):
      os.makedirs(destination)

    for item in os.listdir(destination):
      item_path = os.path.join(destination, item)

      if os.path.isfile(item_path) or os.path.islink(item_path):
        os.remove(item_path)
      elif os.path.isdir(item_path):
        shutil.rmtree(item_path)

    for item in os.listdir(source):
      source_item = os.path.join(source, item)
      destination_item = os.path.join(destination, item)

      if os.path.isfile(source_item):
        shutil.copy(source_item, destination_item)
        print(f"Copied file: {source_item} to {destination_item}")
      if os.path.isdir(source_item):
        copy_to_destination(source = source_item, destination = destination_item)
    return True
  except Exception as e:
    print(f"An error occured: {e}")
    return False




