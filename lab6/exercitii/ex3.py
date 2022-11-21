# Write a function that receives as a parameter a string of text characters and a list of regular expressions and
# returns a list of strings that match on at least one regular expression given as a parameter.

import re


def match_a_regex(text, regex_list):
    return [word for word in re.findall(r'\w+', text) if any([re.match(regex, word) for regex in regex_list])]


def main():
    print(match_a_regex("Some text with t2 numbers and 4 1000r words", [r'\w\d', r'\d+']))


if __name__ == '__main__':
    main()
