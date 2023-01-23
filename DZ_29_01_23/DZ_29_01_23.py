

class Money:
    """
    Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
    В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
    поле для хранения копеек (центы, евроценты, копейки
    и т.д.).
    Реализовать методы для вывода суммы на экран, задания значений для частей.
    """

    def __init__(self, name, whole, fractional, sign):
        self.name = name
        self.__whole = whole
        self.__fractional = fractional
        self.sign = sign

    @property
    def money(self):
        print(f'{self.__whole}.{self.__fractional}')

    def __str__(self):
        return f'{self.__whole}.{self.__fractional} {self.sign}'


d = Money('руб', 13, 50, '\u20BD')
d.money
print(d)
