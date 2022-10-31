import os
import sys 



def extensions():

    try:

        assert(len(sys.argv)>1),"Invalid number of parameters"
        assert(os.path.isdir(sys.argv[1])),"Invalid director"

        directory_path = sys.argv[1]
    
        dir_list = os.listdir(directory_path)
        files = [ os.path.splitext(f)[1][1:] for f in dir_list if os.path.isfile(os.path.join(directory_path,f)) and os.path.splitext(f)[1]]
        return sorted(set(files))

    except Exception as e:
        print(str(e))
        return []


def main():
    print(extensions())


if __name__ == "__main__":
    main()


# python EX4.py "C:\Users\Bianca\Downloads"