
def dictionary_from_string(my_string):
    return {i: my_string.count(i) for i in my_string} 


def main():
    print(dictionary_from_string("Ana has apples."))


if __name__ == '__main__':
    main()