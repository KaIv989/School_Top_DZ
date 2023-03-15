from DZ_19_03_23 import Number
import unittest


class Test_number(unittest.TestCase):
    def setUp(self): #спец функция, здесь при запуске мы можем провести какую то подготовку,
        #например создать экземпляр какого то класса
        self.t_num1 = Number([1, 2, 3, 4, 5])
        self.t_num2 = Number([1, 2, -3, 4, 5])
        self.t_num3 = Number([1, 2, 0, 4, 5])
        self.t_num4 = Number([1, 2, 13, 4, 5])
        self.instances = [self.t_num1, self.t_num2, self.t_num3, self.t_num4]

    def test_sum(self):
        for i in self.instances:
            with self.subTest():
                self.assertEqual(i.sum_num(), sum(i.number))

    def test_sr(self):
        for i in self.instances:
            with self.subTest():
                self.assertEqual(i.sr_num(), sum(i.number) / len(i.number))

    def test_max(self):
        for i in self.instances:
            with self.subTest():
                self.assertEqual(i.max_num(), max(i.number))

    def test_min(self):
        for i in self.instances:
            with self.subTest():
                self.assertEqual(i.min_num(), min(i.number))


if __name__ == '__main__':
    unittest.main


