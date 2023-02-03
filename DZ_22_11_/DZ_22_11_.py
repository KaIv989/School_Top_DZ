
def nod(num1, num2, flag = False):
    if num1 > num2:
        num1, num2 = num2, num1
    if (not flag and num2 % num1 == 0) or (flag % num1 == 0 and num2 % num1 == 0):
        return num1
    if not flag:
        return nod(num1//2, num2, flag = num1)
    return nod(num1 - 1, num2, flag = flag)


def fact(num):
    if num < 2:
        if num < 0:
            return 'Число должно быть положительное'
        return 1
    return num * fact(num - 1)


try:
    x, y = int(input('Введите число №1 ')), int(input('Введите число №2 '))
    print(nod(x, y))

    f = int(input('Введите число для вычисления факториала '))
    print(fact(f))
except RecursionError:
    print('Превышена максимальная глубина рекурсии')
except ValueError:
    print('Вы ввели не число')

