arr1 = input().split()
arr2 = input().split()
sett = set(arr1) & set(arr2)
res = list(map(str, sett)) # не понятно что тут делать с map нуно....???? ни чего лучше не придумал как преобразовать строки еще раз в строки....
print(*res)
#ИЛИ
print(' '.join(res))
print(*list(filter(lambda x: int(x) % 2 == 0, res)))




