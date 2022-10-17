
#------------EX1:  LIST OF THE FIRST N NUMBERS OF THE FIBONACCI STRING-----------------

def fib1(n):
    if n == 1:
        return 1
    if n == 2:
        return [1, 1]
    a = 1
    b = 1
    list = [a, b]
    while len(list) < n:
        c = a + b
        a = b
        b = c
        list.append(c);
    return list


def fib2(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def main():
    print("Insert n : ")
    n = int(input())
    print("Var1: ", fib1(n))
    my_generator = fib2(n)
    print("Var2: ")
    for i in my_generator:
        print(i)

if __name__ == '__main__':
    main()
