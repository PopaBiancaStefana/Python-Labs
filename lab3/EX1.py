
def operations(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return [set1.intersection(set2), set1.union(set2), set1.difference(set2), set2.difference(set1)]


def main():
    print(operations([1, 2, 3, 4], [3, 4, 5, 6]))


if __name__ == '__main__':
    main()