def task_1():
    print('''“Don't compare yourself with anyone in this world… 
if you do so, you are insulting yourself.”
                                        Bill Gates''')


task_1()


def task_2(num_1, num_2):
    for i in range(num_1 + 1, num_2):
        if i % 2 == 0:
            print(i, end = ' ')
    print()


task_2(2, 9)


def task_3(l, s, b):
    matrix = [[s for _ in range(l)] for _ in range(l)]
    if b:
        for i in matrix:
            print(*i)
    else:
        for i in range(l):
            if l - 1 > i > 0:
                for j in range(1, l-1):
                    matrix[i][j] = ' '
            print(*matrix[i])


task_3(4, 5, True)


def task_4(*args):
    return min(args)


print(task_4(434, 5, 7, 89, 5))


def task_5(r_1, r_2):
    res = 1
    if r_1 > r_2:
        r_1, r_2 = r_2, r_1
    for i in range(r_1, r_2 + 1):
        res *= i
    return res


print(task_5(8, 4))


def task_6(num):
    return len(str(num))


print(task_6(4534))


def task_7(num):
    s = str(num)
    return s == s[::-1]


print(task_7(123321))
