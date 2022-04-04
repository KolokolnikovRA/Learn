f = ['Москва','Санкт-Петербург','Калининград','Омск','Тюмень','Новосибирск','Владивосток','Владикавказ','Морской']
print(f)
del f[1]#Удаляет обьект под номером
print(f)
f.append('Новороссийск')
print(f)
f.insert(0,'Еще Москва')
print(f)
f.remove('Еще Москва')#Удаляет первое похожее
print(f)
end = f.pop()
print(end)
print(f)
print(id(f))
a = f.copy()
print(id(a))
print(f.count('Москва'))
print(f.index('Москва'))
f = ['Москва','Санкт-Петербург','Калининград','Омск','Тюмень','Новосибирск','Владивосток','Владикавказ','Морской']
f.sort()
print(f)
f = [6,5,4,7,5,3,2,1]
f.sort()
print(f)
print(f.pop(0))
f.reverse()
print(f)
sp = ['+7912123456', '+7915213456', '+6915213456', '+4915213456', '+7915213456']
sp_new = []
for i in sp:
    if '+7' in i:
        continue
    else:
        sp_new.append(i)
print(sp_new)

spi = [1,2,3,4,5,6,7,8,9,0]
spi_new = []
n = int(input('Вводи количество итераций'))
for i in range(n):
    a = spi.pop(0)
    spi_new = spi
    spi_new.append(a)
print(spi_new)


a = []
while True:
    x = int(input())
    if x != 0:
        a.append(x**2)
    else:
        break
print(a)