def count(*args, **dict_elements):
    nr = 0
    for i in args:
        if i in dict_elements.values():
            nr += 1
    return nr


def main():
    print(count(1, 2, 3, 4, x=1, y=2, z=3, w=5))


if __name__ == '__main__':
    main()
