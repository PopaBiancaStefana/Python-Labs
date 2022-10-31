def validate_dict(rules, dictionary):
    for rule in rules:
        if rule[0] not in dictionary:
            return False
        if (not dictionary[rule[0]].startswith(rule[1])) and rule[1]:
            return False
        if (not dictionary[rule[0]].endswith(rule[3])) and rule[3]:
            return False
        if rule[2] not in dictionary[rule[0]][len(rule[1]):-len(rule[3])] and rule[1] and rule[3]:
            return False
    return True


def main():
    print(validate_dict([("key1", "", "inside", ""), ("key2", "start", "middle", "winter")],
                        {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
    print(validate_dict([("key1", "", "inside", ""), ("key2", "start", "middle", "winter")],
                        {"key1": "come inside, it's too cold out", "key2": "start and middle and winter"}))


if __name__ == '__main__':
    main()
