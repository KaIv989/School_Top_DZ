
def task_1():
    print('''“Don't let the noise of others' opinions
drown out your own inner voice.”
                                Steve Jobs''')


task_1()


def task_2(num_1, num_2):
    for i in range(num_1 + 1, num_2):
        if i % 2 != 0:
            print(i, end = ' ')
    print()


task_2(2, 9)


def task_3(length, vector, symbol): #По классике в задании не прописаны четко условия задачи(( .
    # Не ясно как должено быть передано направление линии, я из прошлого ЗД взял ту же идею за основу.
    # если True - то Горизонт, если False - то вертикаль.
    s = str(symbol) * length
    if vector:
        print(s)
    else:
        for i in s:
            print(i)


task_3(5, True, 5)


def task_4(*args):
    return max(args)


print(task_4(434, 5, 7, 89, 5))


def task_5(r_1, r_2):
    if r_1 > r_2:
        r_1, r_2 = r_2, r_1
    return sum(range(r_1, r_2 + 1))


print(task_5(8, 4))


def task_6(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(task_6(2))


def task_7(num):
    if len(str(num)) != 6:
        return 'Введите шести значное число'
    x = [int(i) for i in str(num)[:3]]
    y = [int(i) for i in str(num)[3:]]
    return sum(x) == sum(y)


print(task_7(123312))


