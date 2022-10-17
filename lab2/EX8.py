# ------------EX8 :FOR EVERY STRING A LIST OF CH. THAT HAVE ASCII % x = 0 OR NOT-------------

def ascii_divisible(lista, x, flag):
    list_of_lists = []
    for word in lista:
        list = []
        for c in word:
            if flag == True:
                if ord(c) % x == 0:
                    list.append(c)
            else:
                if ord(c) % x != 0:
                    list.append(c)
        list_of_lists.append(list)

    return list_of_lists


def main():
    print(ascii_divisible(["test", "hello", "lab002"], 2, False))


if __name__ == '__main__':
    main()
