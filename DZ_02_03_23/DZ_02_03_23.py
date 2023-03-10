from abc import ABC, abstractmethod


class PizzaDoughDepth:
    thin = 'thin'
    thick = 'THICK'


class PizzaDoughType:
    wheat = 'WHEAT'
    corn = 'CORN'
    rye = 'RYE'


class PizzaSauceType:
    pesto = 'PESTO'
    white = 'WHITE_GARLIC'
    barbeque = 'BARBEQUE'
    tomato = 'TOMATO'


class PizzaTopLevelType:
    mozzarella = 'MOZZARELLA'
    salami = 'SALAMI'
    bacon = 'BACON'
    mushrooms = 'MUSHROOMS'
    shrimps = 'SHRIMPS'


"""
Класс компонуемого продукта
"""


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
        self.cooking_time = None  # in minute

    def __str__(self):
        info: str = f"Pizza name: {self.name} \n" \
                    f"dough type: {self.dough} & " \
                    f"{self.dough}\n" \
                    f"sauce type: {self.sauce} \n" \
                    f"topping: {self.topping} \n" \
                    f"cooking time: {self.cooking_time} minutes"
        return info


"""
Абстрактный класс, задающий интерфейс строителя
"""


class Builder(ABC):

    @abstractmethod
    def prepare_dough(self) -> None: pass

    @abstractmethod
    def add_sauce(self) -> None: pass

    @abstractmethod
    def add_topping(self) -> None: pass

    @abstractmethod
    def get_pizza(self) -> Pizza: pass

"""
Реализация конкретных строителей (шеф-поваров) для сборки пицц
"""


class MargaritaPizzaBuilder(Builder):

    def __init__(self):
        self.pizza = Pizza("Margarita")
        self.pizza.cooking_time = 15

    def prepare_dough(self) -> None:
        self.pizza.dough = PizzaDoughDepth.thin

    def add_sauce(self) -> None:
        self.pizza.sauce = PizzaSauceType.tomato

    def add_topping(self) -> None:
        self.pizza.topping.extend(
            [
                it for it in (PizzaTopLevelType.mozzarella,
                              PizzaTopLevelType.mozzarella,
                              PizzaTopLevelType.bacon,
                              )
            ]
        )

    def get_pizza(self) -> Pizza:
        return self.pizza


class SalamiPizzaBuilder(Builder):

    def __init__(self):
        self.pizza = Pizza("Salami")
        self.pizza.cooking_time = 10

    def prepare_dough(self) -> None:
        self.pizza.dough = PizzaDoughDepth.thick

    def add_sauce(self) -> None:
        self.pizza.sauce = PizzaSauceType.barbeque

    def add_topping(self) -> None:
        self.pizza.topping.extend(
            [
                it for it in (PizzaTopLevelType.mozzarella,
                              PizzaTopLevelType.salami,
                              )
            ]
        )

    def get_pizza(self) -> Pizza:
        return self.pizza

"""
Класс Director, отвечающий за процесс поэтапного приготовления пиццы
"""
class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_pizza(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.prepare_dough()
        self.builder.add_sauce()
        self.builder.add_topping()


if __name__ == '__main__':
    director = Director()
    for i in (MargaritaPizzaBuilder, SalamiPizzaBuilder):
        builder = i()
        director.set_builder(builder)
        director.make_pizza()
        pizza = builder.get_pizza()
        print(pizza)
        print('---------------------------')
