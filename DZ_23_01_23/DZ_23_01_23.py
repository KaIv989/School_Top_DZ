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
    # Меняем местами если указан не верный порядок чисел
    if x > y:
        x, y = y, x
    if y < 3:
        return [i for i in range(2, y+1)]
    # Через генератор создаем список сразу без четных
    arr = [i for i in range(2, y+1) if i % 2 or i == 2]
    count = 1

    while count - 1 <= len(arr)//10:  # оптимизация для ускорения работы программы.
        value = arr[count]
        arr = list(filter(lambda e: (e == value or e % value) and e > x, arr))
        count += 1
    return arr


print(prime_numbers(0, 100000))
