import os
import sys


def write_in_file():
    directory, file = sys.argv[1], sys.argv[2]

    try:
        with open(file, "w") as f:
            for (root, directories, files) in os.walk(directory):
                for fileName in files:
                    if fileName[0] == "A":
                        full_file_name = os.path.join(root, fileName)
                        f.write(full_file_name + "\n")
    except Exception as e:
        print(str(e))


def main():
    write_in_file()


if __name__ == "__main__":
    main()

# python EX2.py "C:\\Users\\Bianca\\Downloads" "C:\Users\Bianca\OneDrive\Desktop\Python\labs\Python_2022-2023\lab4\file.txt"
