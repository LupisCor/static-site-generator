import re


def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    urls = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return urls