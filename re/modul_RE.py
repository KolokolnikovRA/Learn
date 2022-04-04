import re
# #
# # text = "Карта map и обьект bitmap - это разные вещи "
# #
# # a = re.findall(r'\bmap\b', text)
# # print(a)
#
# text = 'еду, победы,  5  бЕда'
# a = re.findall(r'[1234567890]', text)
# print(a)
#
#
# text = 'еду,c3 победы,5 7 бЕда'
# a = re.findall(r'[0-9]', text)
# print(a)
#
#
# text = 'еду, победы, бЕда'
# a = re.findall(r'[^, 0-9]', text)
# print(a)
#
#
# text = 'Еда, беду, из-за, победа'
# a = re.findall(r'[-0-9]', text)
# print(a)
#
#
#
# text = 'еду, победы, бЕда'
# a = re.findall(r'[а-яА-Я0-9]', text)
# print(a)
#
#
# text = '(еда), победа, беда'
# a = re.findall(r'[(]еда[)]', text)
# print(a)
# print("_"*40)
# text = '(еда), победа, беда'
# a = re.findall(r'.', text)
# print(a)
#
# text = '(еда), победа, беда'
# a = re.findall(r'\w', text)
# print(a)

# text = "Google, Gooogle, Gooooogle"
# a = re.findall(r'Go{3,4}gle', text)
# print(a)

# text = "89293653059, +79293653059. \n 892936530598, Roman, Роман"
# a = re.findall(r'\W', text)
# print(a)

# text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
# print(text)
# a = re.findall(r"(\w+)\s*=\s*([^;]+)", text)
# print(a)

text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
a = re.findall(r"\w+\s*=\s*[^;]+", text)
print(a)

# text = "Картинка <img.src='bg.jpg'> в тексте</p>"
# a = re.findall(r"<img.*?>", text)
# print(a)
