"""
Дописать код с урока
1) В класс Model добавить: метод для добавления новых статей (с записью в файл), метод подсчета количества статей у одного автора
2) В классы View и Control добавить необходимые методы для поддержки функционала из 1)
"""

import sys


class Article:
    def __init__(self, name, author, cnt_symb, pub_name='', descrip=''):
        self.name = name
        self.author = author
        self.cnt_symb = cnt_symb
        self.pub_name = pub_name
        self.descrip = descrip

    def __str__(self):
        return f'{self.__dict__}'


class Model:
    @staticmethod
    def _wright_txt(path, text):
        with open(path, 'a',  encoding='utf-8') as f:
            f.write('\n' + text)
        return ['запись завершена']
    @staticmethod
    def _read_txt(path):
        data = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                data.append(line.replace('\n', ''))
        return data

    @staticmethod
    def _str_to_Article(list_txt):
        data = []
        for line in list_txt:
            buf = Article(*line.split(','))
            data.append(buf)
        return data

    @staticmethod
    def new_article(path):
        data = Model._read_txt(path)
        return Model._str_to_Article(data)


class View:
    @staticmethod
    def print_list(plist):
        for i in plist:
            print(i)

    @staticmethod
    def print_select_menu():
        print('Выбор действия')
        print('2 - записать новую статью в файл')
        print('1 - Вывести все статьи')
        print('0 - Выйти из программы')


class Control:
    @staticmethod
    def menu():
        View.print_select_menu()
        buf = input()
        adress = './1test.txt'
        if buf == '1':
            res = Model.new_article(adress)
            View.print_list(res)
        elif buf == '2':
            text = input('введите текст статьи')
            res = Model._wright_txt(adress, text)
            View.print_list(res)

        elif buf == '0':
            sys.exit()


while True:
    Control.menu()
