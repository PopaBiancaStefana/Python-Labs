
def build_xml_element(tag, content, **elements):
    xml_element = "<" + tag
    for key, value in elements.items():
        xml_element += " " + key + "=\"" + value + "\""
    xml_element += ">" + content + "</" + tag + ">"
    return xml_element


def main():
    print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))


if __name__ == '__main__':
    main()

