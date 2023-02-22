class Stack:
    """
        Задание 2
    """
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.indicator = 0

    def push(self, value):
        if not self.full():
            self.stack.append(value)
            self.indicator += 1
            return f'Добавили строку в стек'
        return f'Стек заполнен, добавление не возможно'

    def stack_read(self):
        if not self.empty():
            self.indicator -= 1
            return self.stack.pop()
        return f'Стек пуст'

    def lenth(self):
        return self.indicator

    def empty(self):
        return self.indicator == 0

    def full(self):
        return self.indicator == self.size

    def clearing(self):
        self.stack = []
        return f'Стек очищен'

    def only_read(self):
        if not self.empty():
            return self.stack[-1]
        return f'Стек пуст'


n = 0
command = 0
while True:
    try:
        if not n:
            n = int(input('Введите размер стека\n'))
            st = Stack(n)
        if not command:
            command = int(input('1) Введите 1, если вы хотите поместить строку в текст;\n'
                                '2) Введите 2, если Вы хотите прочитать строку из стека;\n'
                                '3) Введите 3, если Вы хотите произвести подсчет количества строк в стеке;\n'
                                '4) Введите 4, если Вы хотите проверку пустой ли стек;\n'
                                '5) Введите 5, если Вы хотите проверку полный ли стек;\n'
                                '6) Введите 6, если Вы хотите очистку стека;\n'
                                '7) Введите 7, для получения значения без выталкивания верхней строки из стека\n'
                                '8) Введите любую другую цифру, для выхода из программы\n'))

        else:
            if command == 1:
                string = input('Введите строку\n')
                print(st.push(string))
                command = 0
            elif command > 7:
                print('Exit')
                break
            else:
                actions = [st.stack_read, st.lenth, st.empty, st.full, st.clearing, st.only_read]
                print(actions[command - 2]())
                command = 0

    except ValueError:
        print('Введите число!')

