#Compare two dictionaries without using the operator "==" returning True or False. dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

def compare_dicts(dict1, dict2):
    if len(dict1) != len(dict2):
        return False
    for key in dict1:
        if key not in dict2:
            return False
        if type(dict1[key]) == dict:
            if not compare_dicts(dict1[key], dict2[key]):
                return False
        elif type(dict1[key]) == list:
            if not compare_lists(dict1[key], dict2[key]):
                return False
        elif type(dict1[key]) == set:
            if not compare_sets(dict1[key], dict2[key]):
                return False
        else:
            if dict1[key] != dict2[key]:
                return False
    return True


def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if type(list1[i]) == dict:
            if not compare_dicts(list1[i], list2[i]):
                return False
        elif type(list1[i]) == list:
            if not compare_lists(list1[i], list2[i]):
                return False
        elif type(list1[i]) == set:
            if not compare_sets(list1[i], list2[i]):
                return False
        else:
            if list1[i] != list2[i]:
                return False
    return True


def compare_sets(set1, set2):
    if len(set1) != len(set2):
        return False
    for i in set1:
        if i not in set2:
            return False
    return True


def main():
    print( compare_dicts({1: {6: 9, 8: 0}, 3: (1,4,6)}, {1: {6: 9, 8: 0}, 3: (1,4,6)}) )
    print( compare_dicts({1: {6: 9, 8: 5}, 3: (1,4,6)}, {1: {6: 9, 8: 0}, 3: [1,4,6,7]}) )
    

if __name__ == '__main__':
    main()