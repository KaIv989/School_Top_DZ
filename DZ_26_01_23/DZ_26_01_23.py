

class MyClass:

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 5

    def __len__(self):# -> Возвращаем количество атрибутов у экземпляра класса
        return len(self.__dict__)


m = MyClass()
m.f = 7

print(len(m))

