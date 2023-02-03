from random import randrange as r


length = 10
l1 = [r(10) for _ in range(length)]
l2 = [r(10) for _ in range(length)]
l3 = [r(10) for _ in range(length)]

tup1 = tuple(l1)
tup2 = tuple(l2)
tup3 = tuple(l3)
print(tup1, tup2, tup3, sep = '\n')

res1 = set(tup1) & set(tup2) & set(tup3)
res2 = set(tup1) ^ set(tup2) ^ set(tup3) - res1
res3 = [tup1[i] for i in range(len(tup1)) if tup1[i] == tup2[i] == tup3[i]]

print(f'результат:\n'
      f'1) элементы, которые есть во всех кортежах: {res1}\n'
      f'2) элементы, которые уникальны для каждого списка: {res2}\n'
      f'3) элементы, которые есть в каждом из кортежей и находятся в каждом из кортежей на той же позиции: '
      f'{res3 if res3 else "Нет таких"}')
