
import json


class Employees:
    def __init__(self, inpt):
        self.inpt = inpt
        self.file = 'data.json'
    def open_file(self):
        with open(self.file, 'r', encoding='utf-8') as read_file:
            data = json.load(read_file)
            return data

