string = 'Hello World!'

print(string.upper())#and
print('Hello World!'.upper())
print(string.lower())
print(string.count('He'))
print(string.find('o'))#Первое вхождение буквы о, ищет вхождение слева на право
print(string.rfind('o'))#Первое вхождение буквы о, ищет вхождение справа на лево
print(string.index('o'))# Если вхождения нет, выдаст ошибку ValueError: substring not found
print(string.find('fgfd'))#выводит -1 если не нашлось вхождения
print(string.replace('He','HHEE'))
string = 'амиосимо'
print(string.isalpha())#Проверка на наличие букв
string = '2343'
print(string.isdigit())#Проверка на наличие цифр

print(string.rjust(10,'&'))

digit = '1,2,3 ,4,5, 6 ,7'
print('_'.join(digit.replace(' ','').split(',')))

digit = '    ghjdkdbv    '
print(digit.strip())#удаляет пробелы слева и справа
print(digit.rstrip())#удаляет только справа пробелы
print(digit.lstrip())#удаляет только слева пробелы



