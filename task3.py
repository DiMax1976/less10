"""""""""
3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка». 
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), 
вычитание (__sub__()), 
умножение (__mul__()), 
деление (__floordiv__, __truediv__()). 
Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление 
до целого числа деления клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., 
где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. 
В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. 
# Тогда метод make_order() вернёт строку: *****\n*****\n*****."""


class Organic_cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):  # сложение. x + y
        return Organic_cell(self.quantity + other.quantity)

    def __sub__(self, other):  # вычитание (x - y).
        if (self.quantity - other.quantity) < 0:

            return f"Substraction error you don't use zero in the values"# {( self.quantity - other.quantity )}"
        else:
            return ( self.quantity - other.quantity )


    def __mul__(self, other):  # умножение (x * y).
        return Organic_cell(self.quantity * other.quantity)

    def __floordiv__(self, other):  # деление (x / y)
            return Organic_cell(self.quantity / other.quantity)

    def __truediv__(self, other):  # целочисленное деление (x // y).
        return Organic_cell(self.quantity // other.quantity)

    def make_order(self, row):
        block_row = self.quantity // row
        res = ''
        for i in range(block_row):
            res += '*' * row + ' \n '
        return res + '*' * (self.quantity % row)


cerullar1 = Organic_cell(10)
cerullar2 = Organic_cell(15)
cerullar3 = Organic_cell(25)
sum_cer = cerullar1 + cerullar2 + cerullar3
sub_cer = cerullar1 - cerullar2
mul_cer=cerullar1 * cerullar2
floordiv_cer=cerullar1 / cerullar2
truediv_cer=cerullar1 // cerullar2
print(sum_cer.quantity)
print(sub_cer)
print(mul_cer.quantity)
print(floordiv_cer.quantity)
print(truediv_cer.quantity)
print(cerullar2.make_order(5))

