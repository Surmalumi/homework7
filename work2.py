# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.


from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param


    @property
    def ready_product(self):
        return str(f'Общая площадь ткани \n'
                   f' {(self.coat()) + (self.suit())}')

    @abstractmethod
    def abstract(self):
        return 'Abstract method'


class Coat(Clothes):
    def ready_product(self):
        return f'Материала всего нужно для пошива пальто: {self.param / 6.5 + 0.5}'

    def abstract(self):
        return 'Abstract method for coat'


class Suit(Clothes):
    def ready_product(self):
        return f'Материала всего нужно для пошива костюма: {2 * self.param + 0.3}'

    def abstract(self):
        return 'Abstract method for suit'


coat = Coat(8)
suit = Suit(2)
print(coat.ready_product())
print(coat.abstract())
print(suit.ready_product())
print(suit.abstract())
