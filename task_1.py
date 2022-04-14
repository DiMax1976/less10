#
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

import numpy


class Matrix:

    def __init__(self, mat):
        self.mat = mat

    def __str__(self):
        matrix_length = len(self.mat)
        matrix_str = ''
        for k in range(matrix_length):
            mat_i = self.mat[k]
            matrix_str = matrix_str + (' '.join([str(i) for i in mat_i])) + '\n'
        return f"{matrix_str}"

    def __add__(self, other):
        if len(self.mat) > len(other.mat):
            while len(self.mat) != len(other.mat):
                if len(self.mat[1]) > len(other.mat[1]):
                    other.mat.append([0] * len(self.mat[1]))
                else:
                    other.mat.append([0] * len(other.mat[1]))

        else:
            while len(self.mat) != len(other.mat):
                if len(self.mat[1]) > len(other.mat[1]):
                    other.mat.append([0] * len(self.mat[1]))
                else:
                    other.mat.append([0] * len(other.mat[1]))
        new_matr=[]

        for n in range(len(self.mat)):
            c = map(sum, zip(self.mat[n] + [0, ] * (x := len(other.mat[n]) - len(self.mat[n])), other.mat[n] + [0, ] * -x))
            new_matr.append(list(c))
        matrix_str2 = ''
        for р in range(len(new_matr)):
            mat_p = new_matr[р]
            matrix_str2 = matrix_str2 + (' '.join([str(i) for i in mat_p])) + '\n'
        return f"{matrix_str2}"



mat1 = [[31, 22],
        [37, 43],
        [51, 86]]
mat2 = [[3, 5, 52],
        [2, 4, 6],
        [-1, 64, -8]]
mat3 = [[3, 5, 8, 3],
        [8, 3, 7, 1]]

neo = Matrix(mat1)
trinity = Matrix(mat2)
morpheus = Matrix(mat3)
print(neo)
print(trinity)
print(morpheus)
new_matrix = trinity + morpheus
print(new_matrix)
new_matrix = neo + trinity
print(new_matrix)
new_matrix = neo + morpheus
print(new_matrix)
#