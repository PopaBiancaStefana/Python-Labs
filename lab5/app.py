from utils import process_item


def main():
    while True:
        x = input("Enter number: ")
        if x == "q":
            return
        
        if x.isnumeric():
            x=int(x)
            print(process_item(x))

        else:
            print("Input must be a number")     


if __name__ == '__main__':
    main()