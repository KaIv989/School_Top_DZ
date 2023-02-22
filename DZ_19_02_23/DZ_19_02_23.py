import pickle
import json


class Plane:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
        self.__poz = 0

    def takeoff(self, height):
        self.__poz = height
        return f'самолет набирает заданную высоту {height} метров'

    def current_height(self):
        return self.poz

    def landing(self):
        self.__poz = 0
        return f'самолет выполняет посадку'

    def loading(self):
        if not self.__poz:
            return f'выполняем посадку пассажиров на борт'
        return f'Посадку пассажиров в воздухе выполнить не возможно!'

    def discharge(self):
        if not self.__poz:
            return f'выполняем высадку пассажиров'
        return f'высадку пассажиров в воздухе выполнить не возможно!'

    def __str__(self):
        return f'Самолет {self.name} пассажировместимостью {self.volume} человек'


air1 = Plane('red', '120')

with open('air1.pickle', 'wb') as f:
    pickle.dump(air1, f)

with open('air1.pickle', 'rb') as f:
    air_new = pickle.load(f)

with open('air1.json', 'w') as f:

    json.dump(air1.__dict__, f)

with open('air1.json', 'r') as f:
    air_new_json = json.load(f)

print(air_new.loading())
print(air_new.takeoff(1000))

print(air_new_json)

print(air_new)
