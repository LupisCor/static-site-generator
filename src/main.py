import os, shutil, sys
from copystatic import copy_static
from generate_page import generate_pages_recursive


source_dir_path = "./static"
dest_dir_path = "./docs"
template_path = "template.html"
dir_path_content = "./content"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    if os.path.exists(dest_dir_path):
        shutil.rmtree(dest_dir_path)

    copy_static(source_dir_path, dest_dir_path)
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath)

    

main()