

class Countrys:
    def __init__(self):
        self.dic = {}

    # Замена и добавление стран
    def new_country(self, name_country='', capital=''):
        if name_country and capital:
            self.dic[name_country] = capital
            print(f'{name_country} со столицей {capital}')
        else:
            print('Вы ввели не корректные данные страны')

    # Поиск
    def search_country(self, name_country=''):
        if self.dic.get(name_country):
            print(f'Столица страны {name_country} - {self.dic[name_country]}')
        else:
            print('Нет такой страны в списке, вы можете ее добавить!')
            self.new_country(name_country, input(f'Введите столицу страны {name_country}: '))

    # Удаление
    def del_country(self, name_country=''):
        if self.dic.get(name_country):
            del self.dic[name_country]
            print(f'{name_country} была успешно удалина из списка')
        else:
            print('Нет такой страны в списке')

    # Выводить на экран весь словарь
    def __str__(self):
        return str(self.dic)


# Пример работы с моей   "программой" в которой реализована возможность:
# добавления, удаления, поиска, замены данных.
a = Countrys()

while True:
    inpt = input('\nДля добавления или замены: Введите через пробел Название страны и ее столицу\n'
                 'Для удаления: Введите через пробел слово "удалить" и название страны\n'
                 'Для поиска: Введите название страны\n'
                 'Для выхода: Введите Y\n').split()
    if not inpt:
        print(a)
        break
    if inpt[0].lower() == 'y':
        print(a)
        break
    if len(inpt) == 2 and inpt[0] != "удалить":
        a.new_country(inpt[0], inpt[1])
    elif len(inpt) == 2 and inpt[0] == "удалить":
        a.del_country(inpt[1])
    elif len(inpt) == 1:
        a.search_country(inpt[0])
    elif len(inpt) > 2:
        print("Вводите данные по очереди, по одной стране")
