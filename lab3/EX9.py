
def count(*args, **dict_elements):
    count = 0
    for i in args:
        if i in dict_elements.values():
            count += 1
    return count


def main():
    print(count(1, 2, 3, 4, x=1, y=2, z=3, w=5))


if __name__ == '__main__':
    main()