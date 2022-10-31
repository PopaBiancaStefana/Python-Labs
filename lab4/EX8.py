import os


def root_files(directory):

    try:
        dir_list = os.listdir(directory)
        return [ os.path.join(directory,f) for f in dir_list if os.path.isfile(os.path.join(directory,f)) ]
  
    except Exception as e:
        print(str(e))
        return []


def main():
    print(root_files("C:\\Users\\Bianca\\OneDrive\\Desktop\\2sem1\\bd"))

if __name__ == "__main__":
    main()