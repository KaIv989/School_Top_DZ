from random import randrange as r
while True:
    try:
        arr_1 = [r(11) for _ in range(int(input('Введите длину первого списка ')))]
        arr_2 = [r(11) for _ in range(int(input('Введите длину второго списка ')))]
        break
    except ValueError:
        print('Нужно вводить числа!')


arr_res_1 = arr_1 + arr_2
arr_res_2 = list(set(arr_res_1))
arr_res_3 = []
arr_res_4_1 = []
arr_res_4_2 = []
arr_res_5_1 = []
arr_res_5_2 = []

for i in arr_1:
    if i in arr_2:
        arr_res_3.append(i)
    else:
        arr_res_4_1.append(i)
for i in arr_2:
    if not (i in arr_1):
        arr_res_4_2.append(i)

arr_res_5_1.extend([min(arr_1), max(arr_1)])
arr_res_5_2.extend([min(arr_2), max(arr_2)])

print(f'список №1: {arr_1}, список №2: {arr_2}')
print(f'1) список, содержащий элементы обоих списков: {arr_res_1}\n'
      f'2) список, содержащий элементы обоих списков без повторений: {arr_res_2}\n'
      f'3) список, содержащий элементы общие для двух списков: {arr_res_3}\n'
      f'4) список, содержащий только уникальные элементы каждого из списков:\n'
      f'уникальные первого списка: {arr_res_4_1}\n'
      f'уникальные второго списка: {arr_res_4_2}\n'
      f'5) список, содержащий только минимальное и максимальное значение каждого из списков:\n'
      f'мин, макс первого списка {arr_res_5_1}\n'
      f'мин, макс второго списка {arr_res_5_2}')



