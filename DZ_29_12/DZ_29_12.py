with open("one.txt", encoding='utf-8') as one, open('new_t.txt', encoding='utf-8') as new:
    while True:
        try:
            str_f_1 = one.__next__()
            str_f_2 = new.__next__()
            if str_f_1 != str_f_2:
                print(f'В первом текстовом файле: {str_f_1}, а во втором: {str_f_2}')
        except StopIteration:
            break


