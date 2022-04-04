# '/Users/Kolokolnikov/PycharmProjects/Learn/aa.txt'
try:
    file = open('..//aa.txt','r', encoding="utf-8")
except FileNotFoundError:
    print('Файла такого нет')

print(file.read())
print('-'*20)
file.seek(0)
print(file.read(4))
print('-'*20)

pos = file.tell()
print(pos)
print('-'*20)
file.seek(0)
for i in file:
    print(i,end='')

file.close()



