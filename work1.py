# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.

class Matrix:


    def __init__(self, matrix_list):
        self.matrix_list = matrix_list


    def __str__(self):
        for line in self.matrix_list:
            for i in line:
                print(f'{i:4}', end='')
            print()
        return ''


    def __add__(self, other):
        for i in range(len(self.matrix_list)):
            for i_1 in range(len(other.matrix_list[i])):
                self.matrix_list[i][i_1] = self.matrix_list[i][i_1] + other.matrix_list[i][i_1]
        return Matrix.__str__(self)


m = Matrix([[5, 2, 5], [2, 5, 2], [1, 1, 1], [2, 0, -2]])
#print(m)
new_m = Matrix([[4, 1, -5], [-3, 1, 3], [0, -2, 2], [-2, 1, 1]])
#print(new_m)
print(m + new_m)