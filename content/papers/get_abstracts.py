import requests
import os
import yaml
import re

def get_paper_abstract(doi):
    # Semantic Scholar API endpoint for paper metadata
    url = f"https://api.semanticscholar.org/v1/paper/{doi}"

    # Make the GET request to fetch paper metadata
    response = requests.get(url)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response

        # Extract metadata (abstract, title, authors, etc.)
        abstract = data.get('abstract', 'No abstract available')
        # title = data.get('title', 'No title available')
        # authors = [author['name'] for author in data.get('authors', [])]
        # year = data.get('year', 'No year available')
        #
        # # Print the metadata
        # print("Title:", title)
        # print("Year:", year)
        # print("Authors:", ", ".join(authors))
        # print("Abstract:", abstract)

        return True, abstract
    else:
        print(f"Error: Unable to retrieve metadata for DOI {doi}. Status code: {response.status_code}")
        return False, ""



def check_abstract_in_front_matter(file_path):
    """
    Check if 'abstract' is defined in the front matter of the markdown file.
    """
    try:
        # Open the markdown file and read its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if the file contains YAML front matter (delimited by ---)
        if content.startswith('---'):
            # Extract the YAML front matter between the '---' delimiters
            front_matter = content.split('---')[1].strip()

            # Parse the YAML front matter
            try:
                front_matter_data = yaml.safe_load(front_matter)
                if isinstance(front_matter_data, dict):
                    # Check if the 'abstract' field is present
                    if 'abstract' in front_matter_data:
                        print(f"Abstract found in: {file_path}")
                        return True
                    else:
                        print(f"No abstract in: {file_path}")
                        return False
                else:
                    print(f"Invalid YAML front matter in: {file_path}")
                    return False
            except yaml.YAMLError:
                print(f"Error parsing YAML front matter in: {file_path}")
                return False
        else:
            print(f"No front matter in: {file_path}")
            return False

        return False

    except Exception as e:
        print(f"Error opening file {file_path}: {e}")
        return False

    return False

def get_doi(link):
    """
    Extracts DOI from a given URL if present. Returns None if no DOI is found.
    """
    # Regular expression to match DOI in the URL
    doi_regex = r"doi\.org/([10.\d{4,9}/\w._;()/:A-Z0-9\-]+)"

    # Search for the DOI pattern in the URL (case-insensitive)
    match = re.search(doi_regex, link.strip(), re.IGNORECASE)

    if match:
        # If a match is found, return the DOI part (without the base URL)
        return match.group(1)
    else:
        # Return None if no DOI is found
        return None


def get_doi_in_front_matter(file_path):
    """
    Check and return 'doi'.
    if there is no doi, returns false.
    """
    try:
        # Open the markdown file and read its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if the file contains YAML front matter (delimited by ---)
        if content.startswith('---'):
            # Extract the YAML front matter between the '---' delimiters
            front_matter = content.split('---')[1].strip()

            # Parse the YAML front matter
            try:
                front_matter_data = yaml.safe_load(front_matter)
                if isinstance(front_matter_data, dict):
                    # Check if the 'abstract' field is present
                    if 'link' in front_matter_data:
                        # print(f"Link found in: {file_path}")

                        # check if "doi" is in link
                        link = front_matter_data["link"]
                        return get_doi(link)
                    else:
                        print(f"No link in: {file_path}")
                        return False
                else:
                    print(f"Invalid YAML front matter in: {file_path}")
                    return False
            except yaml.YAMLError:
                print(f"Error parsing YAML front matter in: {file_path}")
                return False
        else:
            print(f"No front matter in: {file_path}")
            return False

        return False

    except Exception as e:
        print(f"Error opening file {file_path}: {e}")
        return False

    return False


def update_markdown_with_abstract(md_file_path, abstract):
    """
    Adds or updates the 'abstract' field in the YAML front matter of a markdown file,
    without modifying any other content in the markdown file.

    Parameters:
    - md_file_path: Path to the markdown file.
    - abstract: The abstract text to be added to the YAML front matter.
    """
    try:
        with open(md_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if YAML front matter exists (denoted by --- at the start and end)
        if content.startswith('---\n'):
            # Extract the front matter and the markdown content
            front_matter_end = content.find('---', 3) + 3
            front_matter = content[3:front_matter_end-3]
            markdown_content = content[front_matter_end:].lstrip()

            # Load the front matter as a dictionary
            front_matter_dict = yaml.safe_load(front_matter)

            # Update the abstract field in the front matter
            front_matter_dict['abstract'] = abstract

            # Rebuild the front matter with updated abstract
            new_front_matter = yaml.dump(front_matter_dict, default_flow_style=False).strip()

            # Rebuild the entire file content with updated front matter
            new_content = f"---\n{new_front_matter}\n---\n{markdown_content}"

        else:
            # No YAML front matter found, so add it with the abstract
            new_content = f"---\nabstract: {abstract}\n---\n{content}"

        # Write the updated content back to the file
        with open(md_file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

        print(f"Successfully updated the abstract in: {md_file_path}")

    except Exception as e:
        print(f"Error: {e}")





def walk_directory_and_check_abstracts(directory):
    """
    Walk through the directory and check each markdown file for abstract in the front matter.
    """
    # Recursively walk through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Process only markdown files
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if not check_abstract_in_front_matter(file_path):
                    print(file_path)
                    doi = get_doi_in_front_matter(file_path)
                    if doi is not None:
                        success, abstract = get_paper_abstract(doi)
                        if success:
                            print("GOT ABSTRACT:")
                            print(abstract)
                            update_markdown_with_abstract(file_path, abstract)



# Example usage:
directory = '.'  # Replace with the directory you want to scan
walk_directory_and_check_abstracts(directory)


# # Example usage:
# doi = "10.1109/ACCESS.2016.2544381"
# get_paper_metadata(doi)
#
