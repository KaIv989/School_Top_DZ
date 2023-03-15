
class Number:
    def __init__(self, number: list = []):
        self.number = number

    def sum_num(self):
        return sum(self.number)

    def sr_num(self):
        return sum(self.number) / len(self.number)

    def max_num(self):
        return max(self.number)

    def min_num(self):
        return min(self.number)

