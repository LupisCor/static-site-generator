from split_blocks import markdown_to_html_node, extract_title
import os
from pathlib import Path

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path) as markdown_file:
        markdown = markdown_file.read()
    with open(template_path) as template_file:
        template = template_file.read()
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(template)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    lst = os.listdir(dir_path_content)
    for pth in lst:
        content_path = os.path.join(dir_path_content, pth)
        dest_path = os.path.join(dest_dir_path, pth)

        if os.path.isfile(content_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(content_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(content_path, template_path, dest_path, basepath)