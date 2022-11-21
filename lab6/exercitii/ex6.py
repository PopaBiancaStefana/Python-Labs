# Write a function that, for a text given as a parameter,
# censures words that begin and end with vowels.
# Censorship means replacing characters from odd positions with *.

import re


def censor(text):
    return re.sub(r'[aeiouAEIOU]\w*[aeiouAEIOU]', lambda x: re.sub(r'\w', '*', x.group(0)), text)


def main():
    print(censor("Acela este un ou alb"))


if __name__ == '__main__':
    main()
