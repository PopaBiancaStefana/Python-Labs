def good_dictionaries(*args, **keywords):

    good_dict = []

    for arg in args:
        if type(arg) == dict:
            if len(arg.keys()) >= 2 and any([True if type(key) == str and len(key) >= 3 else False for key in arg.keys()]):
                good_dict.append(arg)

    for kw in keywords.keys():
        if type(keywords[kw]) == dict:
            if len(keywords[kw].keys()) >= 2 and any([True if type(key) == str and len(key) >= 3 else False for key in keywords[kw].keys()]):
                good_dict.append(keywords[kw])

    return good_dict


def main():
    print(good_dictionaries( {1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3],{'abc': 4, 'def': 5},3764,dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},test={1: 1, 'test': True}))

if __name__ == '__main__':
    main()