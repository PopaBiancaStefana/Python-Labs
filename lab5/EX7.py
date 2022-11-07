
def sum_digits(n):
    return sum([int(i) for i in str(n)])


def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return [1, 1]
    a = 1
    b = 1
    my_list = [a, b]
    while len(list) < n:
        c = a + b
        a = b
        b = c
        list.append(c)
    return my_list


def process(**keywords):

    fibo_list = fibonacci(1000)
    if "filters" in keywords.keys():
        fibo_list = [f for f in fibo_list if all([p(f) for p in keywords["filters"]])]

    if "offset" in keywords.keys():
        fibo_list = fibo_list[keywords["offset"]:]

    if "limit" in keywords.keys():
        return fibo_list[:keywords["limit"]]
    return fibo_list


def main():
    print(process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2, offset=2))


if __name__ == '__main__':
    main()