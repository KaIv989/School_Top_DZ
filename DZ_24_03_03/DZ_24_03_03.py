import random
import threading


adress1 = './1test.txt' # Специально не стал делать что бы пользователь с клавиатуры вводил путь к файлу, если кому то это нужно вставьте это: input('Введите путь')
adress2 = './2test.txt'
adress3 = './3test.txt'

def record(adress, data = '', fun = ''):
    
    with open(adress, 'w', encoding='utf-8') as f:
        if data:
            print(f'запись {fun}')
            f.write(data)
            print(f'Закончили запись {fun}')
        else:
            print('Создаем 1-й файл с рандомными числами')
            arr = random.sample(range(1, 50), 5)
            f.write(','.join(str(x) for x in arr))
            print('Завершили запись 1-го файла')
    return 'Запись завершена'

def opn():
    with open(adress1, 'r') as f:
        str = f.read()
    return str.split(',')

def prime():
    print('Начинаем вычисления простых чисел')
    result_prime = 'Простые числа: '
    for i in opn():
        i = int(i)
        for j in range(2, i):
            if i % j == 0:
                break
            if j + 1 == i:
                result_prime += str(i) + ', '  
    print('Закончили вычисление простых чисел')
    return record(adress2, result_prime, 'простых чисел')

def fact():
    print('Начинаем вычисления факториалов')
    result_fact = 'Факториалы: '
    for i in opn():
        i = int(i)
        res = 1
        for j in range(1, i+1):
            res *= j
        result_fact += str(res) + ', ' 
    print('Закончили вычисление факториалов')
    return record(adress3, result_fact, 'факториалов')


task1 = threading.Thread(target=record, args=(adress1,))
task2 = threading.Thread(target=prime)
task3 = threading.Thread(target=fact)

task1.start()
task1.join()

task3.start()
task2.start()


