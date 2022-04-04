from random import randint
#
#
# class voin():
#
#     def make_healt(self,healt):
#         self.healt = healt
#
#     def make_hit(x):
#         x.healt -=20
#
# first = voin()
# second = voin()
# first.healt = 100
# second.healt = 100
#
# while first.healt > 0 and second.healt > 0:
#     n = random.randint(1,2)
#     if n == 1:
#         voin.make_hit(first)
#         print('Второй ударил первого')
#         print('У первого ', first.healt)
#     else:
#         voin.make_hit(second)
#         print('Первый ударил второго')
#         print('У второго ', second.healt)
#
# if first.healt > second.healt:
#     print('Первый выйграл')
# else:
#     print('Второй выйграл')

# class Person():
#     def __init__(self,v,n):
#         self.name = v
#         self.surname = n
#
# a = Person('Roman', 'Kolokolnikov')
# print(a.name,a.surname)
#
# class Person:
#     def __init__(self, n, s, q=1):
#         self.name = n
#         self.surname = s
#         self.skill = q
#
#     def __del__(self):
#         print("До свидания, мистер", self.name, self.surname)
#
#     def info(self):
#         return "{} {}, {}".format(self.name, self.surname, self.skill)
#
#
# worker = Person("И", "Котов", 3)
# helper = Person("Д", "Мышев", 1)
# maker = Person("O", "Рисов", 2)
# print(worker.info())
# print(helper.info())
# print(maker.info())
# del helper
# print("Конец программы")
# input()

class Person():
    count = 0

    def __init__(self,c):
        self.id = Person.count
        Person.count += 1
        self.command = c

class Hero(Person):
    def __init__(self,c):
        Person.__init__(self,c)
        self.level = 1

    def up_level(self):
        self.level +=1

class Soldier(Person):
    def __init__(self,c):
        Person.__init__(self,c)
        self.my_hero = None
    def follow(self, hero):
        self.hero = hero.id


h1 = Hero(1)
h2 = Hero(2)

army1 = []
army2 = []

for i in range(20):
    n = randint(1,2)
    if n == 1:
        army1.append(Soldier(n))
    else:
        army2.append(Soldier(n))
print(len(army1), len(army2))
if len(army1) > len(army2):
    h1.up_level()
elif len(army2) > len(army1):
    h2.up_level()

army1[0].follow(h1)

