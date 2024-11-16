
import os
import yaml
from fuzzywuzzy import fuzz

def extract_title_from_frontmatter(file_path):
    """Extracts the title from the YAML frontmatter of a markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        print(f"Skipping {file_path}: Unable to decode file")
        return None

    if not (lines and lines[0].strip() == "---"):
        return None  # Skip files without YAML frontmatter

    # Find the end of YAML frontmatter
    yaml_end_idx = 1
    while yaml_end_idx < len(lines) and lines[yaml_end_idx].strip() != "---":
        yaml_end_idx += 1

    if yaml_end_idx >= len(lines):
        return None  # No closing `---`, skip

    # Parse YAML frontmatter to get the title
    try:
        frontmatter = yaml.safe_load("".join(lines[1:yaml_end_idx]))
        title = frontmatter.get("title", None)
        return title
    except yaml.YAMLError:
        return None  # Skip if YAML parsing fails

def find_similar_titles(directory, similarity_threshold=80):
    """Finds and prints files with duplicate or similar titles in a directory."""
    titles = {}
    duplicates = []

    # Walk through the directory recursively
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):  # Only process .md files
                file_path = os.path.join(root, file)
                title = extract_title_from_frontmatter(file_path)
                if title:
                    # Check for exact duplicate titles first
                    if title in titles:
                        duplicates.append((file_path, title))
                    else:
                        # Compare with all previously seen titles for similarity
                        for seen_title, seen_file in titles.items():
                            similarity = fuzz.ratio(title.lower(), seen_title.lower())
                            if similarity >= similarity_threshold:
                                duplicates.append((file_path, title, seen_file, seen_title, similarity))

                        titles[title] = file_path

    # Print duplicates
    if duplicates:
        print("Files with duplicate or similar titles:")
        for entry in duplicates:
            if len(entry) == 2:
                print(f"Exact duplicate: Title: '{entry[1]}' found in {entry[0]}")
            elif len(entry) == 5:
                print(f"Similar title: '{entry[1]}' in {entry[0]} and '{entry[3]}' in {entry[2]} (Similarity: {entry[4]}%)")
                print("\n")
    else:
        print("No duplicate or similar titles found.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Find and print Markdown files with duplicate or similar titles.")
    parser.add_argument("directory", help="Directory to scan for markdown files with duplicate or similar titles")
    parser.add_argument("--threshold", type=int, default=80, help="Threshold for similarity percentage (default: 80%)")
    args = parser.parse_args()

    find_similar_titles(args.directory, args.threshold)
