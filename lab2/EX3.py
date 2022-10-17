# -------------EX3: 2 LISTS, INTERSECTION, REUNION, SUBTRACTION -------

def read_list():
    input_string = input()
    list = input_string.split()
    for i in range(len(list)):
        # convert each item to int type
        list[i] = int(list[i])
    return list


# complexity O(n)
# set() converts any of the iterable to sequence of iterable elements with distinct elements
def a_intersected_b(list_a, list_b):
    s = set(list_b)
    return [value for value in list_a if value in s]


# use the set() function on both the lists
def a_reunited_b(list_a, list_b):
    return list(set(list_a) | set(list_b))


def a_minus_b(list_a, list_b):
    s = set(list_b)
    return [value for value in list_a if value not in s]


def main():
    print('Enter elements of the first list separated by space: ')
    list_a = read_list()
    print('Enter elements of the second list separated by space: ')
    list_b = read_list()
    print('a intersected with b', a_intersected_b(list_a, list_b))
    print('a reunited with b ', a_reunited_b(list_a, list_b))
    print('a minus b ', a_minus_b(list_a, list_b))
    print('b minus a', a_minus_b(list_b, list_a))


if __name__ == '__main__':
    main()
