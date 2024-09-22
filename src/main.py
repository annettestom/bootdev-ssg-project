from copy_source_to_destination import copy_to_destination
from generate_recursively import generate_pages_recursive

def main():
  source_dir = "static/"
  dest_dir = "public/"

  print("Starting the static site generator...")

  if copy_to_destination(source_dir, dest_dir):
    print("Static files copied successfully!")
  else:
    print("Something went wrong!")

  if generate_pages_recursive("content", "content", "template.html", "public"):
    print("Page generated successfully!")
  else:
    print("Something went wrong")

if __name__ == "__main__":
  main()