# Write a function that recursively scrolls a directory and displays those files whose name matches
# a regular expression given as a parameter or contains a string that matches the same expression.
# Files that satisfy both conditions will be prefixed with ">>"

import re
import os


def good_files(directory, regex):
    result = []
    for root, dirs, files in os.walk(directory):
        for f in files:

            ok = 0
            if re.search(regex, f):
                file_name = os.path.join(root, f)
                try:
                    with open(file_name, "r") as f_d:
                        for line in f_d:
                            if re.search(regex, line):
                                ok = 1
                                break
                except Exception as e:
                    print(e)
                    continue

                if ok == 0:
                    result += [f]
                else:
                    result += [">>" + f]

    return result


def main():
    print(good_files("C:\\Users\\Bianca\\OneDrive\\Desktop\\Python\\labs\\Python_2022-2023\\lab6\\exercitii", r'ex\d+'))


if __name__ == '__main__':
    main()
