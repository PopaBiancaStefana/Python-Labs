import os
from EX5 import search_target
 
def search_target_2(target,to_search,callback):
    try:
        return search_target(target,to_search)

    except Exception as e:
        callback(e)
        return []
    

def callback_function(e):
    print(str(e))


def main():
    print(search_target_2("C:\\Users\\Bianca\\OneDrive\\Desktop\\Python\\labs\\Python_2022-2023\\lab4\\file.txt", "Algorithm",callback_function))
    print(search_target_2("C:\\Users\\Bianca\\OneDrive\\Desktop\\Python\\labs\\Python_2022-2023\\lab4", "Algorithm",callback_function))
if __name__ == "__main__":
    main()