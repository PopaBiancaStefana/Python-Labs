
def even_odd(my_list):
    return list(zip([i for i in my_list if i % 2 == 0], [i for i in my_list if i % 2 != 0]))

def main():
    print(even_odd([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

if __name__ == '__main__':
    main()
