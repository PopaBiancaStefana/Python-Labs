
def number_elements(my_list):
    return [i for i in my_list if type(i) in [int, float, complex]]


def main():
    print(number_elements([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
    

if __name__ == '__main__':
    main()