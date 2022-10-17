# -----------EX2: THE PRIME NUMBERS FROM A LIST--------------------------

def read_list():
    input_string = input('Enter elements of the list separated by space: ')
    list = input_string.split()
    for i in range(len(list)):
        # convert each item to int type
        list[i] = int(list[i])
    return list


def is_prime(x):
    if x == 1:
        return True
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False

    return True


def all_prime_nr(my_list):
    return list(filter(is_prime, my_list))


def main():
    my_list = read_list()
    prime_list = all_prime_nr(my_list)
    if len(prime_list) == 0:
        print('\nThere are no prime numbers ')
    else:
        print('\nThe list of prime numbers : ', prime_list)


if __name__ == '__main__':
    main()
