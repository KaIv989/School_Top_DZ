

class Car:
    """Задание 1
    Реализуйте класс «Автомобиль». Необходимо хранить
    в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
    методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса. """

    def __init__(self, name, year_release, brand, v, color, price):
        self.name = name
        self.year_release = year_release
        self.brand = brand
        self.v = v
        self.color = color
        self.__price = price

    def change(self, arg, value):
        self.__dict__[arg] = value

    def __str__(self):
        return f'{self.__dict__}'


kia = Car('Cerato', 2010, 'kia', '1.6', 'red', 650000)
print(kia.name, kia.brand, kia.color)

kia.change('name', 'civic')
kia.change('brand', 'honda')
kia.change('color', 'black')
kia.change('__price', 1)
kia.__price = 550000
print(kia.name, kia.brand, kia.color, kia.__price)
print(kia)
