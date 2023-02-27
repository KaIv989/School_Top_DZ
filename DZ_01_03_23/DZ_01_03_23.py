from abc import ABC, abstractmethod


class Pasta(ABC):
    @abstractmethod
    def type_pasta(self, ):
        pass

    @abstractmethod
    def sauce(self):
        pass

    @abstractmethod
    def filling(self):
        pass

    @abstractmethod
    def supplements(self):
        pass


class Creamy(Pasta):
    def type_pasta(self):
        return f'Паста в сливочно-сырном соусе'

    def sauce(self):
        return f'феттуччине с пармезаном и сливочным маслом.'

    def filling(self):
        return f'Паста - это макароны а не пельмени, какая в них может быть начинка?'

    def supplements(self):
        return f'помимо лапши, сыра и масла в этом рецепте используются и жирные сливки.'
    def __str__(self):
        return f'Тип - {self.type_pasta()}, соус - {self.sauce()}, добавки: {self.supplements()}'


class Pesto(Pasta):
    def type_pasta(self):
        return f'Паста с соусом песто из зеленого горошка'

    def sauce(self):
        return f'очень вкусный и яркий соус песто из зеленого горошка, свежей мяты, пармезана и творожного сыра.'

    def filling(self):
        return f'Паста - это макароны, а не пельмени, какая в них может быть начинка?'

    def supplements(self):
        return f'горошек зелёный, сыр творожный, сыр пармезан, мята свежая, чеснок, сок лимона, масло оливковое, перец чёрный молотый, соль, ракушки макароны.'

    def __str__(self):
        return f'Тип - {self.type_pasta()}, соус - {self.sauce()}, добавки: {self.supplements()}'


class Bolognese(Pasta):
    def type_pasta(self):
        return f'Паста с Классическим соусом болоньезе'

    def sauce(self):
        return f'Молочный соус болоньезе готовится долго, на медленном огне.'

    def filling(self):
        return f'Паста - это макароны, а не пельмени, какая в них может быть начинка?'

    def supplements(self):
        return f'фарш мясной, помидоры консервированные, лук репчатый, морковь, стебель сельдерея, вино красное сухое,'\
               f' сливки, масло оливковое, соль, перец чёрный молотый.'

    def __str__(self):
        return f'Тип - {self.type_pasta()}, соус - {self.sauce()}, добавки: {self.supplements()}'


class FactoryPasta:
    def param(self, type_pasta):
        if type_pasta == 'Creamy':
            return Creamy()
        elif type_pasta == 'Pesto':
            return Pesto()
        elif type_pasta == 'Bolognese':
            return Bolognese()


factory = FactoryPasta()
prod1 = factory.param('Creamy')
prod2 = factory.param('Pesto')
prod3 = factory.param('Bolognese')
print(prod1)
print(prod2)
print(prod3)
