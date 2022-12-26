
def task_1():

    """Дано два текстовых файла. Выяснить, совпадают ли
    их строки. Если нет, то вывести несовпадающую строку
    из каждого файла."""

    with open("task1.txt", encoding='utf-8') as task1, open('cop_task1.txt', encoding='utf-8') as cop_task1:
        while True:
            try:
                str_f_1 = task1.__next__()
                str_f_2 = cop_task1.__next__()
                if str_f_1 != str_f_2:
                    print(f'В первом текстовом файле: {str_f_1}, а во втором: {str_f_2}')
            except StopIteration:
                break


def task_2():

    """Дан текстовый файл. Необходимо создать новый файл
    и записать в него следующую статистику по исходному
    файлу:
    ■ Количество символов;
    ■ Количество строк;
    ■ Количество гласных букв;
    ■ Количество согласных букв;
    ■ Количество цифр.
    """
    vowel = 0
    consonant = 0
    digit = 0
    other = 0
    with open('task2.txt', 'w',  encoding='utf-8') as task2, open('task1.txt', 'r', encoding='utf-8' ) as task1:
        r = task1.read()
        print(f'1) Количество символов: {len(r)}', file = task2)
        task1.seek(0)
        print(f'2) Количество строк: {len([*task1])}', file = task2)
        
        for i in r:
            if i in 'а, у, о, ы, э, я, ю, ё, и, е':
                vowel += 1
            elif i in 'б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ':
                consonant += 1
            elif i.isdigit():
                digit += 1
            else:
                other += 1
        print(f'3) Гласных: {vowel}', file = task2)
        print(f'4) Согласных: {consonant}', file = task2)
        print(f'5) Цифр: {digit}', file = task2)
        print(f'6) Прочие символы: {other}', file = task2)


def task_3():

    """Дан текстовый файл. Удалить из него последнюю
    строку. Результат записать в другой файл."""

    with open('task3.txt', 'w',  encoding='utf-8') as task3, open('task1.txt', 'r', encoding='utf-8' ) as task1:
        print(*[*task1][:-1], sep ='', file = task3)


def task_4():

    """Дан текстовый файл. Найти длину самой длинной
    строки."""

    lenth = 0
    with open('task1.txt', 'r', encoding='utf-8' ) as task1:
        for i in task1:
            if lenth < len(i):
                res = i
                lenth = len(i)
        print('длина самой длинной строки:', lenth, 'символов')
        print('строка:', res)


def task_5(word):

    """Дан текстовый файл. Посчитать сколько раз в нем
    встречается заданное пользователем слово."""

    with open('task1.txt', 'r', encoding='utf-8' ) as task1:
        print(f'{word} встречается {task1.read().count(word)} раз(а).')


def task_6(word, word_new):

    """Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется
    пользователем."""

    with open('task1.txt', 'r', encoding='utf-8') as task1, open('task6.txt', 'w', encoding='utf-8') as task6:
        read = task1.read()
        count = read.count(word)
        print(f'{word} встречается {count} раз(а).')
        if count == 0:
            return
        while True:
            try:
                substitutions = int(input(f'Сколько слов вы хотите поменять? Введите число от 1-{count}\n'))
                if 0 < substitutions <= count:
                    task6.write(read.replace(word, word_new, substitutions))
                    break
                print('Введите корректное число замен!')
            except ValueError:
                print('Введите корректное число замен!')
                
    with open('task6.txt', 'r', encoding='utf-8') as task6:
        print(task6.read())


task_1()
task_2()
task_3()
task_4()
task_5('реже')
task_6('реже', 'чаще')