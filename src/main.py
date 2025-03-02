import os
import shutil
from markdown_to_htmlnode import *
from textnode import *
from parentnode import *
from leafnode import *
from textnode import *
from pathlib import Path
import sys

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def extract_title(markdown):
    title = markdown.split("\n\n")[0]
    if title.count("#") != 1:
        raise Exception("No title!")
    else:
        return title[2:]
    
def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    with open(from_path) as f:
        contents = f.read()
    html_string = markdown_to_htmlnode(contents).to_html()
    with open(template_path) as tmp:
        temp_contents = tmp.read()
        title = extract_title(contents)
    finished = temp_contents.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    finished = temp_contents.replace('href = "/', f'href = "/{basepath}').replace('src = "/', f'src = "/{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(finished)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

    
              

def main():
    if len(sys.argv[1]) > 0:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    copy_files_recursive("static/", "docs/")
    generate_pages_recursive("content/", "template.html", "./docs", basepath)
main()