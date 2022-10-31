import os
import sys

def last_20_lines( file_name ):
    try:
        with open(file_name, "r") as f:
            lines = f.read()
            print(lines)
            return lines[-20:]

    except Exception as e:
        print(str(e))



def problem3( my_path ):

    if os.path.isfile(my_path):
        return last_20_lines(my_path)

    elif os.path.isdir(my_path):   
        extensions = {}
        for (root, directories, files) in os.walk(my_path):
            for fileName in files:
                extension = os.path.splitext(fileName)[1]
                if extension  in extensions:
                    extensions[extension] +=1
                else:
                    extensions[extension] = 1
        return list(extensions.items())
    else:
        raise Exception("Invalid parameter.")


def main():

    print(problem3("C:\\Users\\Bianca\\OneDrive\\Desktop\\MinimProm.txt"))
    # print(problem3("C:\\Users\\Bianca\\Downloads"))

if __name__ == "__main__":
    main()