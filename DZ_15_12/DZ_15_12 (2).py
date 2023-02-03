
dic = {'a1': 3, 'a2': 15, 'a3': 7, 'a4': 10, 'a5': 1, 'a6': 2, 'a7': -5, 'a8': 34, 'a9': 12}


# переводим наш словарь в список кортежей, отправляем на сортировку по половине изначального словаря
# пока не останется по одному элементу
# после этого начинаем сортировать наши списки и соединять их по алгоритму слияния в функции merge_sort_2().
def mergesort(dic1):
    if isinstance(dic1, dict):
        dic1 = [i for i in dic1.items()]
        flag = True    # Это для того чтобы в конце перевести обратно в словарь.
    else:
        flag = False
    if len(dic1) > 1:
        crushing = len(dic1)//2
        if flag:
            return dict(merge_sort_2(mergesort(dic1[:crushing]), mergesort(dic1[crushing:])))
        return merge_sort_2(mergesort(dic1[:crushing]), mergesort(dic1[crushing:]))
    else:
        return dic1


def merge_sort_2(arr1, arr2):
    res = []
    x = arr1.pop(0)
    y = arr2.pop(0)
    while True:
        if y[1] > x[1]:
            res.append(y)
            if not arr2:
                res.append(x)
                res.extend(arr1)
                return res
            y = arr2.pop(0)
        else:
            res.append(x)
            if not arr1:
                res.append(y)
                if arr2:
                    res.extend(arr2)
                return res
            x = arr1.pop(0)


print(mergesort(dic))
