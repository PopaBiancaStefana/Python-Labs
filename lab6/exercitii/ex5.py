# Write another variant of the function from the previous exercise that returns those elements
# that have at least one attribute that corresponds to a key-value pair in the dictionary.

import re


def get_xml_elements(path, attrs):
    # print("".join([f"{key} = \"{value}\" " for key, value in attrs.items()]))
    with open(path, "r") as f:
        text = f.readlines()
        for line in text:
            if re.search(r"[^<]\w\s*\w\s*\w\s=\s\"\w+\"", line) \
                    and any([re.search(f"{key} = \"{value}\"", line) for key, value in attrs.items()]):
                print(line)


def main():
    get_xml_elements("ex4.xml", {"class": "url", "name": "url-form", "data-id": "item"})


if __name__ == '__main__':
    main()
