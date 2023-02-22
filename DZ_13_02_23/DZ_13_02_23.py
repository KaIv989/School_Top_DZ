class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.indicator = 0

    def push(self, value):
        if not self.full():
            self.stack.append(value)
            self.indicator += 1
            return f'Добавили строку в стек'

    def stack_read(self):
        if not self.empty():
            self.indicator -= 1
            return self.stack.pop()

    def lenth(self):
        return self.indicator

    def empty(self):
        return self.indicator == 0

    def full(self):
        return self.indicator == self.size

    def clearing(self):
        self.stack = []

    def only_read(self):
        return self.stack[-1]


st = Stack(3)
st.push('efe')
st.push('efege')
st.push('yjhuy')

print(st.stack_read())
print(st.stack_read())
print(st.stack_read())
