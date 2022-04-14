# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, H, V):
        self.H = H
        self.V = V

    def __str__(self):
        return f"{self.fabric}"

    def __add__(self, other):
        return f"Total fabric costs: {self.fabric + other.fabric}"

    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):
    @property
    def fabric(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):
    @property
    def fabric(self):
        return 2 * self.H + 0.3



coat_fabric = Coat(50, 175)
suit_fabric = Suit(50, 180)

print(coat_fabric)
print(suit_fabric)
print(coat_fabric+suit_fabric)

