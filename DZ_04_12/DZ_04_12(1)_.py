class Basketball_players:
    def __init__(self, name = False, height = False):
        self.dic = {}
        self.new_player(name, height)


# Замена и добавление игроков, допускается создавать игрока без указания его роста, не допускается рост передавать строкой!!!
    def new_player(self, name = False, height = False):
        if name and isinstance(height, (float, int)):
            self.dic[name] = height
        else:
            print('Вы ввели не корректные данные игрока')

# Поиск игроков по имени
    def search_player(self, name = None):
        if self.dic.get(name):
            print(f'Рост {name} - {self.dic[name]}')
        else:
            print('Нет такого баскетболиста в списке')
# Удаление играков по имени
    def del_player(self, name = None):
        if self.dic.get(name):
            del self.dic[name]
        else:
            print('Нет такого баскетболиста в списке')
# Выводить на экран весь словарь
    def __str__(self):
        return str(self.dic)




# Пример работы с моей   "программой" в которой реализована возможность:
    # добавления, удаления, поиска, замены данных.

a = Basketball_players("Майкл Джордан", 198)
a.new_player("Мэджик Джонсон", 206)
a.new_player("Шакил О’Нил", 216)
a.new_player("Карим-Абдул Джаббар", 213)
a.del_player("Карим-Абдул Джаббар")
a.del_player("Карим-Абдул Джаббар")
print(a)
a.del_player()
a.search_player("Шакил О’Нил")
a.search_player("Карим-Абдул Джаббар")

b = Basketball_players('Карим Абдул-Джаббар')
print(b)




