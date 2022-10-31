import os

#-------------------------

def search_in_file(target, to_search):
     with open(target,"r") as my_file:
        text = my_file.read()
        return to_search in text
   

def search_target(target,to_search):
    if os.path.isfile(target):
        if search_in_file(target,to_search):
            return [target]
        else:
            return []
    elif os.path.isdir(target):
        result = []
        for root,directories,files in os.walk(target):
            for fileName in files:
                name = os.path.join(root,fileName)
                if search_in_file(name,to_search):
                   result.append(name)
        return result
    else:
        raise ValueError("Target needs to be file or directory")


def main():
    # files = search_for_target( "C:\Users\Bianca\OneDrive\Desktop\Python\labs\Python_2022-2023\lab4", "Users")
    print(search_target("C:\\Users\\Bianca\\Downloads", "Player"))

if __name__ == "__main__":
    main()

    