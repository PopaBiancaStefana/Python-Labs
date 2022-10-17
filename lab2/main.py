import numpy as np


# -----------------LAB 2----------------------------------------------


# ------------EX1:  LIST OF THE FIRST N NUMBERS OF THE FIBONACCI STRING-----------------

# def fib1(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return [1, 1]
#     a = 1
#     b = 1
#     list = [a, b]
#     while len(list) < n:
#         c = a + b
#         a = b
#         b = c
#         list.append(c);
#     return list
#
#
# def fib2(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
#
# def main():
#     print("Insert n : ")
#     n = int(input())
#     print("Var1: ", fib1(n))
#     my_generator = fib2(n)
#     print("Var2: ")
#     for i in my_generator:
#         print(i)
#
# if __name__ == '__main__':
#     main()

# -----------EX2: THE PRIME NUMBERS FROM A LIST--------------------------

# def read_list():
#     input_string = input('Enter elements of the list separated by space: ')
#     list = input_string.split()
#     for i in range(len(list)):
#         # convert each item to int type
#         list[i] = int(list[i])
#     return list
#
#
# def is_prime(x):
#     if x == 1:
#         return True
#     for i in range(2, x//2+1):
#         if x%i == 0:
#             return False
#
#     return True
#
#
# def all_prime_nr(list):
#     prime_list = []
#     for i in range(len(list)):
#         if is_prime(list[i]):
#             prime_list.append(list[i])
#     return prime_list
#
#
# def main():
#     list = read_list()
#     prime_list = all_prime_nr(list)
#     if len(prime_list) == 0:
#         print('\nThere are no prime numbers ')
#     else:
#         print('\nThe list of prime numbers : ', prime_list)
#
#
# if __name__ == '__main__':
#     main()

# -------------EX3: 2 LISTS, INTERSECTION, REUNION, SUBTRACTION -------

# def read_list():
#     input_string = input()
#     list = input_string.split()
#     for i in range(len(list)):
#         # convert each item to int type
#         list[i] = int(list[i])
#     return list


## complexity O(n)
## set() converts any of the iterable to sequence of iterable elements with distinct elements
# def a_intersected_b(list_a, list_b):
#     s = set(list_b)
#     return [value for value in list_a if value in s]
#
#
# # use the set() function on both the lists
# def a_reunited_b(list_a, list_b):
#     return list(set(list_a) | set(list_b))
#
#
# def a_minus_b(list_a, list_b):
#     s = set(list_b)
#     return [value for value in list_a if value not in s]
#
#
# def main():
#     print('Enter elements of the first list separated by space: ')
#     list_a = read_list()
#     print('Enter elements of the second list separated by space: ')
#     list_b = read_list()
#     print('a intersected with b', a_intersected_b(list_a,list_b))
#     print('a reunited with b ', a_reunited_b(list_a,list_b))
#     print('a minus b ', a_minus_b(list_a,list_b))
#     print('b minus a', a_minus_b(list_b,list_a))
#
#
# if __name__ == '__main__':
#     main()

# --------EX4: compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]------

# def compose(musical_notes, moves, start):
#     song = [musical_notes[start]]
#     current_pos = start
#     for move in moves:
#         current_pos += move
#         song.append(musical_notes[current_pos % len(musical_notes)])
#     return song
#
#
# def main():
#     print(compose(['do','re','mi','fa','sol'],[1,-3,4,2],2))
#
#
# if __name__ == '__main__':
#     main()


# --------EX5: REPLACE ALL ELEMENTS UNDER THE MAIN DIAGONAL WITH 0 IN MATRIX------

# def read_matrix(m):
#     a = []
#     for i in range(m):
#         a.append([])
#         for j in range(m):
#             a[i].append(int(input('A[' + str(i) + ',' + str(j) + ']: ')))
#     return a
#
#
# def replace(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if i > j:
#                 matrix[i][j] = 0
#     return matrix
#
#
# def main():
#     m = int(input("insert nr of rows/columns: "))
#     a = read_matrix(m)
#     print("Var1: ", np.triu(a))
#     print("Var2: ", replace(a))
#
#
# if __name__ == '__main__':
#     main()

# -------------------EX 6--------------------------

# def appear_x_times(x, lists):
#     appear_x_times_list = []
#     # items that appear in the lists
#     appear_in_lists = []
#
#     for list in lists:
#         for item in list:
#                 appear_in_lists.append(item)
#
#     for item in appear_in_lists:
#         if item not in appear_x_times_list and appear_in_lists.count(item) == x:
#             appear_x_times_list.append(item)
#
#     return appear_x_times_list
#
#
# def main():
#     print(appear_x_times(2, [[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]]))
#
#
# if __name__ == '__main__':
#     main()

# ------------EX7: NR OF PALINDROME NUMBERS & THE GREATEST PALINDROME FROM LIST------
#
# def is_palindrome(nr):
#     if str(nr) == str(nr)[::-1]:
#         return True
#     return False
#
#
# def nr_palindromes_and_greatest(a_list):
#     counter = 0
#     greatest = 0
#     for i in a_list:
#         if is_palindrome(i):
#             counter += 1
#             if i > greatest:
#                 greatest = i
#     return [counter, greatest]
#
#
# def read_list():
#     input_string = input('insert list of elements separated by comma: ')
#     new_list = input_string.split(',')
#     for i in range(len(new_list)):
#         new_list[i] = int(new_list[i])
#     return new_list
#
#
# def main():
#     new_list = read_list()
#     print(nr_palindromes_and_greatest(new_list))
#
#
# if __name__ == '__main__':
#     main()


# ------------EX8 :FOR EVERY STRING A LIST OF CH. THAT HAVE ASCII % x = 0 OR NOT-------------

# def ascii_divisible(lista, x, flag):
#     list_of_lists = []
#     for word in lista:
#         list = []
#         for c in word:
#             if flag == True:
#                 if ord(c) % x == 0:
#                     list.append(c)
#             else:
#                 if ord(c) % x != 0:
#                     list.append(c)
#         list_of_lists.append(list)
#
#     return list_of_lists
#
# def main():
#     print(ascii_divisible(["test", "hello", "lab002"], 2, False))
#
#
# if __name__ == '__main__':
#     main()

# --------------------EX 9-----------------------------------
# def cant_see_game(matrix):
#     positions = []
#     for i in range(1, len(matrix) - 1):
#         for j in range(0, len(matrix[i]) - 1):
#             if matrix[i][j] < matrix[i - 1][j]:
#                 positions.append((i, j))
#
#     return positions
#
#
# def main():
#     matrix = [[1, 2, 3, 2, 1, 1],
#
#               [2, 4, 4, 3, 7, 2],
#
#               [5, 5, 2, 5, 6, 4],
#
#               [6, 6, 7, 6, 7, 5]]
#     print(cant_see_game(matrix))
#
#
# if __name__ == '__main__':
#     main()

# -------------------EX 10------------------------------------

def list_of_tuples(*args):
    list_of_tuples = []
    list_of_lists = []

    #creez lista de liste
    for i in args:
        list_of_lists.append(i)

    for i in range(len(list_of_lists[0])):
        tuple = []
        for j in range(len(list_of_lists)):
            if i < len(list_of_lists[j]):
                tuple.append(list_of_lists[j][i])
        list_of_tuples.append(tuple)

    return list_of_tuples


def main():
    print(list_of_tuples([1, 2, 3, 4], [5, 6, 7], ["a", "b", "c"]))


if __name__ == '__main__':
    main()

# ------------------EX 11-------------------------------------
#
# def sort_by(list_tuples):
#     for i in range(0, len(list_tuples)-1):
#         for j in range(i + 1, len(list_tuples)):
#             a = list_tuples[i]
#             b = list_tuples[j]
#             if a[1][2] > b[1][2]:
#                 list_tuples[i] = b
#                 list_tuples[j] = a
#     print(list_tuples)
#
#
# def sort_by_v2(list_tuples):
#     list_tuples.sort(key=lambda i: i[1][2])
#     return  list_tuples
#
#
# def main():
#     print('Var1: ')
#     sort_by([('abc', 'bcd'), ('abc', 'zza')])
#     print('Var2: ')
#     lista = [('abc', 'bcd'), ('abc', 'zzb'), ('abc', 'zza')]
#     print(sort_by_v2(lista))
#
#
# if __name__ == '__main__':
#     main()


# ------------------------EX 12----------------------------------

# def group_by_rhyme(words):
#     #dictionary
#     rhyme_dict = {}
#
#     for word in words:
#         last_two_letters = word[-2:]
#         if last_two_letters not in rhyme_dict:
#             rhyme_dict[last_two_letters] = [word] #letters - key, word - value
#         else:
#             rhyme_dict[last_two_letters].append(word)
#     return rhyme_dict
#
#
# def main():
#     print(group_by_rhyme(['ana', 'banana', 'oana', 'carte', 'arme', 'parte']))
#
#
# if __name__ == '__main__':
#     main()
