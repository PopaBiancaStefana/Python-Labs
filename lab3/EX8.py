def loop(mapping):
    my_list = []
    key = mapping["start"]
    while key not in my_list:
        my_list.append(key)
        key = mapping[key]
    return my_list


def main():
    print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


if __name__ == '__main__':
    main()
