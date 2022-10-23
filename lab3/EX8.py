
def loop(mapping):
    list = []
    key = mapping["start"]
    while key not in list:
        list.append(key)
        key = mapping[key]
    return list


def main():
    print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


if __name__ == '__main__':
    main()
