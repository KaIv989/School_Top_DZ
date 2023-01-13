import time


def decorator(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        print(time.time() - start, 'секунд')
        return result
    return wrapper


@decorator
def prime_numbers(x = 0, y = 1000):
    # Меняем местами если указан не верный диапазон чисел
    if x > y:
        x, y = y, x
    # Если диапазон до 3, то сразу возвращаем результат (исключая 0)
    if y < 4:
        if x < 1:
            x = 1
        return list(range(x, y+1))
    # Через генератор создаем список сразу без четных
    arr = [i for i in range(x, y+1) if i % 2 or i == 2]
    count = 2

    while count <= len(arr)//3:  # оптимальное условия для больших и маленьких диапазонов.
        value = arr[count]
        arr = list(filter(lambda e: e == value or e % value, arr))
        count += 1
    return arr


print(prime_numbers(0, 10000))
