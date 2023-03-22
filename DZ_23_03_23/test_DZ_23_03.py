from DZ_23_03_23 import Number
import unittest


class Test_number(unittest.TestCase):
    def setUp(self): #спец функция, здесь при запуске мы можем провести какую то подготовку,
        #например создать экземпляр какого то класса
        self.num = Number()
        self.arr = [48, -1, 0, 33]

    def test_num(self):
        for i in self.arr:
            self.num.record(i)
            self.assertEqual(self.num.calculus_system_8(), oct(i))
            self.assertEqual(self.num.calculus_system_16(), hex(i))
            self.assertEqual(self.num.calculus_system_2(), bin(i))

    


if __name__ == '__main__':
    unittest.main

