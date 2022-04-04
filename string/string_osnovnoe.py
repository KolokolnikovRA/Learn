srt_1 = 'Привет!!'
srt_2 = ''' Привет!
Я Учу Питон,
у нас все получится'''
print(' Привет \n Роман на новой строке')
str_3 = srt_1
print(str_3)
print('_'*20)

s = 'abracadabraabracadabraabracadabra'
a = 'asd' in s
b = '4' in s
c = 'a' in s
d = 'ab' in s
print(a)
print(b)
print(c)
print(d)
print('_'*20)

print('ABC' == 'abc')
print('abc' == 'abc')
print('AVC' != 'avc')
print('_'*20)

psw = 'pass'
in_psw = ''
while in_psw != psw:
    in_psw = input('Введите пароль!\n')
print('Вход выполнен!')

