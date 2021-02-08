# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)


    def __add__(self, other):
        return self.quantity + other.quantity


    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Результат отрицательный')


    def __mul__(self, other):
        return self.quantity * other.quantity


    def __truediv__(self, other):
        return self.quantity // other.quantity


    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\\n'
        result += '*' * (self.quantity % row) + '\n'
        return result



cell = Cell(12)
cell_2 = Cell(5)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(5))

