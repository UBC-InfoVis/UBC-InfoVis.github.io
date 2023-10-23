# by Matt I.B. Oddo - 2023.10.21

import yaml
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)


def extract_titles(yaml_file):
    with open(yaml_file, "r") as file:
        data = yaml.safe_load(file)
    titles = []
    for idx, entry in enumerate(data):
        if "title" in entry:
            titles.append(entry["title"])
        else:
            print(idx, "NO TITLE!")
    return titles


titles = extract_titles("publications.yml")

# for title in titles:
#     print(title)
#     print()
