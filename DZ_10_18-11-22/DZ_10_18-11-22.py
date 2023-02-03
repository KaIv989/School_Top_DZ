import string

def hash_gen(s: str):
    '''генератор хэштегов'''
    res = '#'
    if s:
        try:
            arr = s.strip().split()
        except AttributeError:
            print('Вводить необходимо текст!')
            return False
        for i in arr:
            res += i.strip(string.punctuation).capitalize()
        if 1 < len(res) <= 140:
            return res
        return False
    return False


print(hash_gen(' Если ввод или результат представляет собой: ^пустую строку, он должен вернуть   !'))
help(hash_gen)

