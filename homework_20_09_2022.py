# '''Каждое из слов «разработка», «сокет», «декоратор» представить в строковом
#  формате и проверить тип и содержание соответствующих переменных. Затем с помощью
#  онлайн-конвертера преобразовать строковые представление в формат Unicode и также
#  проверить тип и содержимое переменных.
# '''
#
# word_1 = 'разработка'
# word_2 = 'сокет'
# word_3 = 'декоратор'
#
# print(type(word_1), type(word_2), type(word_3))
#
# word_1_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
# word_1_2 = '\u0441\u043e\u043a\u0435\u0442'
# word_1_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
#
#
# print(word_1_1, word_1_2, word_1_3)
# print(word_1 == word_1_1)
#
# '''Каждое из слов «class», «function», «method» записать в байтовом типе
#  без преобразования в последовательность кодов
#  (не используя методы encode и decode) и определить тип, содержимое и длину
#   соответствующих переменных.
# '''
#
# word_4 = b'class'
# word_5 = b'function'
# word_6 = b'method'
#
# print('тип - ', type(word_4), '; длинна - ', len(word_4))
# print('тип - ', type(word_5), '; длинна - ', len(word_5))
# print('тип - ', type(word_6), '; длинна - ', len(word_6))
#
# '''Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе'''
#
# word_7 = b'attribute'
# # word_8 = b'класс' - на это слово вылетает ошибка
# # word_9 = b'функция' - на это слово вылетает ошибка
# word_10 = b'type'
#
# ''' Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
# строкового представления в байтовое и выполнить обратное преобразование (используя
# методы encode и decode).
# '''
#
# word_21 = 'разработка'
# a = word_21.encode('utf-8')
# print(a)
# b = bytes.decode(a, 'utf-8')
# print(b)
#
# word_22 = 'администрирование'
# aa = word_22.encode('utf-8')
# print(aa)
# bb = bytes.decode(aa, 'utf-8')
# print(bb)
#
# word_23 = 'protocol'
# aaa = word_23.encode('utf-8')
# print(aaa)
# bbb = bytes.decode(aaa, 'utf-8')
# print(bbb)
#
# word_24 = 'standard'
# aaaa = word_24.encode('utf-8')
# print(aaaa)
# bbbb = bytes.decode(aaaa, 'utf-8')
# print(bbbb)
#
# ''' Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
# байтовового в строковый тип на кириллице.
# '''
#
# import subprocess
# args = ['ping', 'yandex.ru']
# subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
# print('#'*100)
#
# for line in subproc_ping.stdout:
#     line = line.decode('cp866').encode('utf-8')
#     print(line.decode('utf-8'))
#
#
#
# args_2 = ['ping', 'youtube.com']
# subproc_ping_2 = subprocess.Popen(args_2, stdout=subprocess.PIPE)
# print('#'*100)
#
#
# for line in subproc_ping_2.stdout:
#     line = line.decode('cp866').encode('utf-8')
#     print(line.decode('utf-8'))
#

##############################################################################################
'''Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл
в формате Unicode и вывести его содержимое'''

import locale

my_string = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w+') as f_n:
    for i in my_string:
        f_n.write(i + '\n')
    f_n.seek(0)

print(f_n)

my_coding = locale.getpreferredencoding()


with open('test_file.txt', 'r', encoding=my_coding) as f_n:
    for i in f_n:
        print(i)

    f_n.seek(0)
