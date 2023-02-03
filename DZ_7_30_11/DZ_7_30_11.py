import string

inpt = input('Введите текст')
count_punctuation = 0
for i in inpt:
    if i in string.punctuation:
        count_punctuation += 1
count_sentences = len(inpt.split('.')) - 1 #Т.к все предложения заканчиваются точкой необходимо исключить последнюю пустую строку
count_word = len(inpt.split())
count_lenth = len(inpt)

print(count_punctuation, count_sentences, count_word, count_lenth, sep = '\n')
