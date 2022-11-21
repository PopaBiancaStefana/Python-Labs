# Write a function that receives as a parameter the path to an xml
# document and an attrs dictionary and returns those elements that
# have as attributes all the keys in the dictionary and values  the corresponding values.
# For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will
# be those tags whose attributes are class="url" si name="url-form" si data-id="item"

import re


def get_xml_elements(path, attrs):
    # print("".join([f"{key} = \"{value}\" " for key, value in attrs.items()]))

    with open(path, "r") as f:
        text = f.readlines()
        for line in text:
            if re.search(r"[^<]\w\s*" + "".join([f"{key} = \"{value}\" " for key, value in attrs.items()]) + ">", line):
                print(line)


def main():
    get_xml_elements("ex4.xml", {"class": "url", "name": "url-form", "data-id": "item"})


if __name__ == '__main__':
    main()
