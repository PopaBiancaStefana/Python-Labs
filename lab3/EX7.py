
def operations(*sets):
    operations_dict = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            operations_dict[str(sets[i]) + " | " + str(sets[j])] = sets[i].union(sets[j])
            operations_dict[str(sets[i]) + " & " + str(sets[j])] = sets[i].intersection(sets[j])
            operations_dict[str(sets[i]) + " - " + str(sets[j])] = sets[i].difference(sets[j])
            operations_dict[str(sets[j]) + " - " + str(sets[i])] = sets[j].difference(sets[i])
    return operations_dict



def main():
    print(operations({1, 2, 3, 4}, {3, 4, 5, 6}))
    

if __name__ == '__main__':
    main()
