import os




def extensions(directory):

    dir_list = os.listdir(directory)
    files = [ os.path.splitext(f)[1][1:] for f in dir_list if os.path.isfile(os.path.join(directory,f)) ]
  
    return sorted(set(files))


def main():
    print(extensions("C:\\Users\\Bianca\\Downloads"))


if __name__ == "__main__":
    main()

