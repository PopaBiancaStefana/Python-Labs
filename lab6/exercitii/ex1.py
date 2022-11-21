# Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters

import re


def extract_words(text):
    return re.findall("[a-zA-Z0-9]+", text)
    # re.findall(r'\w+', text)


def main():
    print(extract_words("Some text with 2 n4mbers and 1000 words"))


if __name__ == '__main__':
    main()
