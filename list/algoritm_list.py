
#Разбивка целого числа на цифры
b= int(input('Вводи'))
d = []
while b:
    d = [b%10] + d
    b //= 10
print(d)

#Программа меняющая местами числа
n = 11
a = list(range(n))
print(a)
for i in range(n//2):
    a[i],a[n-i-1] = a[n-i-1],a[i]
print(a)

#Программа сортировки метода выбора(пузырька)

b = [-4,-6,-9,0,7,6,9,4,5,6]
n = len(b)
for i in range(n-1):
    for j in range(i+1,n):
        if b[i] > b[j]:
            b[i],b[j] = b[j],b[i]
print(b)

#Алгоритм Евклида( наибольшего общего делителя)

x = int(input('1-number'))
y = int(input('2-number'))
sx = x; sy = y
while x != y:
    if x > y:
        x -= y
    else:
        y -= x

print(sx,sy,x)

#Быстрый алгоритм Евклида!

x = int(input('1-number'))
y = int(input('1-number'))
sx = x; sy = y
x = max(sx,sy)
y = min(sx,sy)
while y:
    x,y = y, x%y
print(sx,sy,x)
