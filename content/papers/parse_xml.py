import xml.etree.ElementTree as ET
import os
import re

import requests
import yaml
from pathlib import Path


# Directory to store markdown files
output_dir = "markdown_files"
os.makedirs(output_dir, exist_ok=True)


def get_bibentry(key):

    url = f"https://dblp.org/rec/{key}.bib"

    response = requests.get(url)
    response.raise_for_status() # check status

    return response.text


def make_file(article):
    # Extract article fields
    key = article.get("key")
    mdate = article.get("mdate")
    authors = [author.text for author in article.findall("author")]
    title = article.find("title").text.strip() if article.find("title") is not None else ""
    pages = article.find("pages").text if article.find("pages") is not None else ""
    year = article.find("year").text if article.find("year") is not None else ""
    volume = article.find("volume").text if article.find("volume") is not None else ""
    journal = article.find("journal").text if article.find("journal") is not None else ""
    booktitle = article.find("booktitle").text if article.find("booktitle") is not None else ""
    ee = article.find("ee").text if article.find("ee") is not None else ""
    url = article.find("url").text if article.find("url") is not None else ""
    stream = article.find("stream").text if article.find("stream") is not None else ""

    # handle journal vs conference
    venue = journal if journal != "" else booktitle

    # create authors list
    authors_list = "\n".join([f"  - {author}" for author in authors])

    # grab the bibentry
    bibcontent = get_bibentry(key)

    # Create Markdown front matter
    front_matter = f"""---
key: {key}
layout: papers
title: "{title}"
date: {mdate}
venue: "{venue}"
authors:
{authors_list}
link: {ee}
bib: |-
{"  " + bibcontent.replace('\n', '\n  ')}
---
"""

    regex = re.compile('[^a-zA-Z\s]')
    title = title.replace("-", " ")
    title = regex.sub('', title).replace(" ", "_")

    filename = f"{year}-{authors[0].split()[-1]}-{title}.md".lower()

    underscore_regex = re.compile('_+')
    filename = underscore_regex.sub('_', filename)

    return front_matter, filename

def parse_and_convert(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()


    for r in root.findall("r"):

        articles = []
        articles += r.findall("article")
        articles += r.findall("inproceedings")


        for article in articles:

            # check if it is an informal type:
            if article.get("publtype") == "informal":
                print(f"SKIPPING {article.find('title').text}")
                continue

            front_matter, file_name = make_file(article)
            file_path = os.path.join(output_dir, file_name)

            print(file_name)

            # Write to Markdown file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(front_matter)

# Example usage
xml_file_path = "articles.xml"  # Replace with your XML file path
parse_and_convert(xml_file_path)
