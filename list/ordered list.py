lst = ['Москва','Самара','Новосибирск','Омск','Челябинск','Псков']

print(lst)
print(lst[3])
lst[4]='Санкт-Петербруг'
print(lst)

f = [['Москва','Санкт-Петербург','Калининград'],['Омск','Тюмень','Новосибирск'],['Владивосток','Владикавказ','Морской']]
print(f[1][1])
print([1,2,3] + ['Москва','Самара'])
digs = [4,3,1,0,4]
digs = digs + [5]
digs += [6]
print(digs)

print('Москва' in lst)
print(max(digs))
print(min(digs))
print(sum(digs))
print(sorted(digs))
print(sorted(digs, reverse=True))

d = [-1, 0, 5, 3, 2]
for i in range(len(d)-1):
    d[i] += 7.2
print(d)

a = [[1,2],[3,4],[5,6]]
b = [[1,0],[0,1],[1,1]]
res = [[0,0],[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        res[i][j] = a[i][j] + b[i][j]
print(res)

k = 1
digit = [0]*k
N = 0; x = 0
while x >= 0 and N < k:
    x = int(input('Вводи\n-'))
    digit[N] = x
    N += 1
print(digit)


s = 0
for i in digit:
    s +=i
s = s/k
print(s)

r = 3
d = [0]*r
n =0
while n < r:
    b = int(input('Вводи числа детка'))
    d[n] = b
    n +=1
print('Есть' if 5 in d else "Отсутствует")
