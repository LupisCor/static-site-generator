import os, shutil, sys
from copystatic import copy_static
from generate_page import generate_page, generate_pages_recursive


source_dir_path = "./static"
dest_dir_path = "./public"
template_path = "template.html"
dir_path_content = "./content"
basepath = sys.argv[0] or "/"

def main():
    if os.path.exists(dest_dir_path):
        shutil.rmtree(dest_dir_path)

    copy_static(source_dir_path, dest_dir_path)
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath)

    

main()