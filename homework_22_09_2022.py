"""1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например,
main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС»,
«Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл
main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv(). """
# import re
# import csv
#
#
# def get_data() -> list:
#
#     path_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
#     list_template = [
#         r'Изготовитель системы:\s+([a-zA-Z]+)',
#         r'Название ОС:\s+([a-zA-Z0-9А-Яа-я\s\.]{1,})[\n]',
#         r'Код продукта:\s+([-0-9a-zA-Z]+)',
#         r'Тип системы:\s+([-0-9a-zA-Z\s]+)[\n]',
#     ]
#     os_prod_list = []
#     os_name_list = []
#     os_code_list = []
#     os_type_list = []
#     main_data = [
#         ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'],
#         [], [], [],
#     ]
#
#     for path in path_list:
#         with open(path, 'r', encoding='cp1251') as f:
#             data = f.read()
#         os_prod_list.append(','.join(re.findall(list_template[0], data)))
#         os_name_list.append(','.join(re.findall(list_template[1], data)))
#         os_code_list.append(','.join(re.findall(list_template[2], data)))
#         os_type_list.append(','.join(re.findall(list_template[3], data)))
#
#     for i in range(len(os_name_list)):
#         main_data[i + 1].append(os_prod_list[i])
#         main_data[i + 1].append(os_name_list[i])
#         main_data[i + 1].append(os_code_list[i])
#         main_data[i + 1].append(os_type_list[i])
#
#     return main_data
#
#
# def write_to_csv(link_to_csv: str, encode: str) -> None:
#     """Записывает данные в csv формате по полученному пути
#     Args:
#         link_to_csv (str): Путь по которому будет сохранен файл, включаа название файла
#         encode (str): кодировка файла
#     """
#     with open(link_to_csv, 'w', encoding=encode) as f:
#         wrtie_csv = csv.writer(f, delimiter=',')
#         data = get_data()
#         wrtie_csv.writerows(data)
#
#
# if __name__ == '__main__':
#     write_to_csv('test.csv', 'utf-8')
#

#########################################################################################################
#
# import json
#
# def write_order_to_json(item, quantity, price, buyer, date) -> None:
#
#     dict_to_json = {
#         'item': item,
#         'quantity': quantity,
#         'price': price,
#         'buyer': buyer,
#         'date': date,
#     }
#
#     with open('orders.json', 'r', encoding='utf-8') as f:
#         orders_list = json.load(f)
#         orders_list['orders'].append(dict_to_json)
#
#     with open('orders.json', 'w', encoding='utf-8') as f:
#         json.dump(orders_list, f, sort_keys=True, indent=4)
#
#
# if __name__ == '__main__':
#     write_order_to_json(
#         item=['продукты', 'канцтовары', 'бижутерия'],
#         quantity=[8, 4, 91],
#         price=[99.00, 78.00, 100.50],
#         buyer=['Инокентий Кетн Никифорович'],
#         date=['22.09.22'])
#
#
######################################################################################################

import yaml

first_key = [
    'kobe bryant 24',
    'michael jordan 23',
    'karl malone 32',
    'stephen curry 30'
]

second_key = 100
third_key = {
    'first_value':  str(100) + u'\u20BD',
    'second_value': str(200) + u'\u20BD',
    'third_value': str(300) + u'\u20BD',
}

to_yaml = {'first_key': first_key, 'second_key': second_key, 'third_key': third_key}

with open('file.yaml', 'w', encoding='utf-16') as f:
    yaml.dump(to_yaml, f, allow_unicode=True, default_flow_style=False, default_style='"')

with open('file.yaml', 'r', encoding='utf-16') as fr:
    print(yaml.safe_load(fr) == to_yaml)