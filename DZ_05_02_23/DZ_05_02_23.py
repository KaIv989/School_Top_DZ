
class Airplane:
    def __init__(self, air_type, max_passengers, passengers):
        self.air_type = air_type
        self.max_passengers = max_passengers
        self.passengers = passengers

    def __int__(self):
        return self.passengers

    def __str__(self):
        return f'Тип самолета: {self.air_type} - макс вместимость: {self.max_passengers}'

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.air_type == other.air_type

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers

    def __add__(self, other):
        if isinstance(other, int):
            self.passengers = self.passengers + other
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            self.passengers = self.passengers - other
        return self


air1 = Airplane('boing', 300, 150)
air2 = Airplane('Tu', 200, 100)
air3 = Airplane('Tu', 200, 150)

print(air1 == air2)
print(air1 < air2)
print(air1 > air2)
print(air3 == air2)
air1 += 12
print(int(air1))
print(air2)
print(air1 == 5)
