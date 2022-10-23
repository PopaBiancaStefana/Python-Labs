
def unique_duplicate(my_list):
    set1 = set(my_list)
    return (len(set1), len(my_list) - len(set1))


def main():
    print(unique_duplicate([1,1,2,2,2,3,4,5,5]))


if __name__ == '__main__':
    main()