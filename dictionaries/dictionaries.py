#
# txt = {'1':'Роман','2':'Дима','3':'Ринат'}
#
# for key, values in txt.items():
#     print(key,values)
#
# k = int(input('Введите количество чисел которые хотите записать в словать'))
# n = 0
# dict_new = {}
# while n < k:
#     i = int(input('Вводите число в словать'))
#     n += 1
#     if i % 2 == 0:
#         dict_new[i] = i ** 2
#
#     else:
#         continue
#
# print(dict_new)
#
# start_line = "int=целое число, dict=словарь, list=список, str=строка, bool=булевый тип" # Начальная строка
# list_string = [['', ''], ['', ''], ['', ''], ['', ''], ['', '']] # Создаю многомерный список
# list_temp = list(start_line.replace('=', ', ').split(', ')) # Удаляю знаки равно и разбиваю по словам. Записываю в временный список
# print(f"Вывожу тест списка: {list_temp}") # Тестирую результат
# index = 0 # Счетчик для работы с временным массивом
#
# # Делаю перебор циклом for с вложенным циклом for для заполнения двумерного списка.
# for i in range(len(list_temp) // 2): # Так как в двумерном списке значения будут находится по два на втором уровне делю на два счетчик, чтобы не выйти за приделы списка.
#     for j in range(0, 2): # Вложенный цикл дает нам возможность заполнить второй уровень списка.
#         list_string[i][j] = list_temp[index]
#         index += 1
#
# dict_one = dict(list_string) # Помещаю в список данные из двумерного списка.
#
# print(f"Вывожу тест словаря: {dict_one}")

#
# dict_translate = dict() # Создаю словарь с помощью функции
# count_user = int(input('Сколько слов с переводом вы хотите сохранить: ')) # Сколько слов хочет внести пользователь
# count = 0 # Счетчик цикла
#
# while count_user > count: # Вводмм данные пользователем
#     word_an_english = input("Введите слов на английском: ") # Слова по английски
#     word_an_russian = input("Введите перевод слова: ") # Слова по русски
#     dict_translate[word_an_english] = word_an_russian # Вносим слова. В словарь в ключ - английское слово, в значение - русское
#     count += 1
#
# print(dict_translate) # Выводим результат

txt = 'Колокольников Роман Александрович'
txt = txt.lower()
dic = {}
for i in txt:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1
print(dic)
