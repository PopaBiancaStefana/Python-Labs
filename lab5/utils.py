#shortest function to find the least prime number greater than the given number 

def process_item(x):
    if x < 2:
        return 2
    else:
        for i in range(x+1, 2*x):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                return i

def main():

    x = int(input("Enter the number:"))
    print(process_item(x))

if __name__ == '__main__':
    main()
