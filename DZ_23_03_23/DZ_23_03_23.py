
class Number:
    def record(self, value: int = None):
        if value or value == 0:
            with open('1test.txt', 'w') as f:
                f.write(str(value))
            return 'Запись завершена '
        with open('1test.txt', 'r') as f:
                num = int(f.read())
        return num
    
    def calculus_system_8(self):
         return oct(self.record())
    
    def calculus_system_16(self):
         return hex(self.record())

    def calculus_system_2(self):
         return bin(self.record())

a = Number()
print(a.record(8))
print(a.calculus_system_8())
