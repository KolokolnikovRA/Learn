
msg = 'Hello world!'

print(msg[2])
print(msg[1:8:2])
print(len(msg))
print(msg[-1])
print(msg[2:10])

copy = msg[::2]

print(id(msg))
print(id(copy))

msg = 'abracadabra'
a = msg.count('a')
print(a)
b = msg.replace('ab','')
print(b)
c = msg.count('ra')
print(c)

d = input("Ввидите предложение")
f = (',').join(d.split(' '))
print(f)

print('Ищем палиндром')
a = input()

if a == a[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')

