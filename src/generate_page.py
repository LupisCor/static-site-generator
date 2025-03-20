from split_blocks import markdown_to_html_node, extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path) as markdown_file:
        markdown = markdown_file.read()
    with open(template_path) as template_file:
        template = template_file.read()
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    print(type(html))
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(template)