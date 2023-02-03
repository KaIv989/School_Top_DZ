arr = ['z', 'qwert', 'qwe', 'q', 'cc', 'aa', 'bb']

def buble_sort(arr):
    for j in range(1, len(arr)):
        for i in range(len(arr)-j):
            if len(arr[i]) > len(arr[i+1]) or (len(arr[i]) == len(arr[i+1]) and arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr




print(buble_sort(arr))


