
# -------------------EX 10------------------------------------

def list_of_tuples(*args):
    list_of_tuples = []
    list_of_lists = []

    #creez lista de liste
    for i in args:
        list_of_lists.append(i)

    for i in range(len(list_of_lists[0])):
        tuple = []
        for j in range(len(list_of_lists)):
            if i < len(list_of_lists[j]):
                tuple.append(list_of_lists[j][i])
        list_of_tuples.append(tuple)

    return list_of_tuples


def main():
    print(list_of_tuples([1, 2, 3, 4], [5, 6, 7], ["a", "b", "c"]))


if __name__ == '__main__':
    main()