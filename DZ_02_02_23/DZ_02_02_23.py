

class Fruts:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    @property
    def type(self):
        if self.name in ['апельсин', 'лимон']:
            return 'цитрусовый'
        return 'не цитрусовый'

    def re_name(self, new_name):
        self.name = new_name

    def re_color(self, new_color):
        self.color = new_color

    def __str__(self):
        return f'{self.color} {self.name}'

    def __del__(self):
        print(self, "был удален")
        del self


f = Fruts('апельсин', 'зеленый')
print(f.type('efe'))
f.re_name('fd')
print(f.type)
print(f)
