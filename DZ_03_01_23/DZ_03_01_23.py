import json


class Employees:
    """Напишите информационную систему «Сотрудники».
    Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
    сотрудника по фамилии, вывод информации обо всех
    сотрудниках, указанного возраста, или фамилия которых
    начинается на указанную букву. Организуйте возможность
    сохранения найденной информации в файл. Также весь
    список сотрудников сохраняется в файл (при выходе из
    программы — автоматически, в процессе исполнения
    программы — по команде пользователя). При старте
    программы происходит загрузка списка сотрудников из
    указанного пользователем файла."""

    def __init__(self):
        self.file = 'data.json'

    def write_file(self, dic):
        staff = self.open_file()
        staff.update(dic)
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)

    def open_file(self):
        with open(self.file, 'r', encoding='utf-8') as file:
            staff = json.load(file)
        return staff

    def input_integer(self, text):
        num = input(text)
        if num.isdigit():
            return int(num)
        print('Вы ввели не число!')
        return self.input_integer(text)


employees = Employees()

try:
    data = employees.open_file()
except FileNotFoundError:
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump({}, file, indent=2)
    data = employees.open_file()

while True:
    search = input('\nВведите фамилию сотрудника\n'
                   'или первую букву на которую начинается фамилия интересующих вас сотрудников\n'
                   'или определенный возраст\n'
                   'или q для выхода и получения информации обо всех сотрудниках: \n')
    if search.lower() == 'q':
        employees.write_file(data)
        print(data)
        break

    if search in data:
        if employees.input_integer('Введите 0, если вы хотите редактировать данные сотрудника\n'
                                   'Введите любое число, если вы хотите посмотреть данные сотрудника  '):
            print(search, data[search])
        else:
            age = employees.input_integer('Введите верный возраст сотрудника  или 0 для удаления  ')
            if age:
                data[search] = age
                print(search, data[search])
            else:
                del data[search]
                print(search, '- Удален!')

    else:
        if search.isalpha() and len(search) == 1:
            for i in data:
                if i[0].lower() == search.lower():
                    print(i, data[i])

        elif search.isdigit():
            for i in data:
                if data[i] == int(search):
                    print(i, data[i])
        else:

            data[search] = employees.input_integer('Введите возраст нового сотрудника  ')
            print('Новый сотрудник', search, data[search])
