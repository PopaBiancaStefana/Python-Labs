
# ------------------------EX 12----------------------------------

def group_by_rhyme(words):
    #dictionary
    rhyme_dict = {}

    for word in words:
        last_two_letters = word[-2:]
        if last_two_letters not in rhyme_dict:
            rhyme_dict[last_two_letters] = [word] #letters - key, word - value
        else:
            rhyme_dict[last_two_letters].append(word)
    return rhyme_dict


def main():
    print(group_by_rhyme(['ana', 'banana', 'oana', 'carte', 'arme', 'parte']))


if __name__ == '__main__':
    main()