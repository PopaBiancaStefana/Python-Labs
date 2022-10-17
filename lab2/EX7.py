
# ------------EX7: NR OF PALINDROME NUMBERS & THE GREATEST PALINDROME FROM LIST------

def is_palindrome(nr):
    if str(nr) == str(nr)[::-1]:
        return True
    return False


def nr_palindromes_and_greatest(a_list):
    counter = 0
    greatest = 0
    for i in a_list:
        if is_palindrome(i):
            counter += 1
            if i > greatest:
                greatest = i
    return [counter, greatest]


def read_list():
    input_string = input('insert list of elements separated by comma: ')
    new_list = input_string.split(',')
    for i in range(len(new_list)):
        new_list[i] = int(new_list[i])
    return new_list


def main():
    new_list = read_list()
    print(nr_palindromes_and_greatest(new_list))


if __name__ == '__main__':
    main()
