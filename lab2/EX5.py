
# --------EX5: REPLACE ALL ELEMENTS UNDER THE MAIN DIAGONAL WITH 0 IN MATRIX------
import numpy as np

def read_matrix(m):
    a = []
    for i in range(m):
        a.append([])
        for j in range(m):
            a[i].append(int(input('A[' + str(i) + ',' + str(j) + ']: ')))
    return a


def replace(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
    return matrix


def main():
    m = int(input("insert nr of rows/columns: "))
    a = read_matrix(m)
    print("Var1: ", np.triu(a))
    print("Var2: ", replace(a))


if __name__ == '__main__':
    main()
