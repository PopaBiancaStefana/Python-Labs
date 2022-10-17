
# ------------------EX 11-------------------------------------

def sort_by(list_tuples):
    for i in range(0, len(list_tuples)-1):
        for j in range(i + 1, len(list_tuples)):
            a = list_tuples[i]
            b = list_tuples[j]
            if a[1][2] > b[1][2]:
                list_tuples[i] = b
                list_tuples[j] = a
    print(list_tuples)


def sort_by_v2(list_tuples):
    list_tuples.sort(key=lambda i: i[1][2])
    return  list_tuples


def main():
    print('Var1: ')
    sort_by([('abc', 'bcd'), ('abc', 'zza')])
    print('Var2: ')
    lista = [('abc', 'bcd'), ('abc', 'zzb'), ('abc', 'zza')]
    print(sort_by_v2(lista))


if __name__ == '__main__':
    main()
