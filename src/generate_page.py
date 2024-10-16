import os
from markdown_blocks import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as f:
        markdown = f.read()
        
    with open(template_path, "r") as f:
        template = f.read()
        
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    
    new_content = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(new_content)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(entry_path) and entry.endswith(".md"):
            dest_path = os.path.join(dest_dir_path, os.path.relpath(entry_path, dir_path_content))
            dest_path = os.path.splitext(dest_path)[0] + ".html"
            generate_page(entry_path, template_path, dest_path)
        elif os.path.isdir(entry_path):
            dest_subdir_path = os.path.join(dest_dir_path, os.path.relpath(entry_path, dir_path_content))
            os.makedirs(dest_subdir_path, exist_ok=True)
            generate_pages_recursive(entry_path, template_path, dest_subdir_path)