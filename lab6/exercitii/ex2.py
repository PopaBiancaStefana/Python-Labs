# ex2: Write a function that receives as a parameter a regex string, a text string and a whole number x,
# and returns those long-length x substrings that match the regular expression.

# Example: regex = r'\w+', text = "Some text with 2 numbers and 1000 words", x = 3

import re


def substrings(regex, text, x):
    return [word for word in re.findall(regex, text) if len(word) == x]


def main():
    print(substrings('\w+', "Some text with 2 numbers and 100 words", 3))


if __name__ == '__main__':
    main()