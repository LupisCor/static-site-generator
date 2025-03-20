import os, shutil
from copystatic import copy_static
from generate_page import generate_page


static_path = "./static"
public_path = "./public"
from_path = "./content/index.md"
template_path = "template.html"
dest_path = "./public/index.html"

def main():
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    copy_static(static_path, public_path)
    generate_page(from_path, template_path, dest_path)

    

main()