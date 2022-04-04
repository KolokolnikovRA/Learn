
#
# fio = input('ФИО через пробел')
# fio = fio.split(' ')
# print(f'''Ваши персональные данные
# Фамилия:{fio[0]}
# Имя:{fio[1]}
# Отчество:{fio[2]}
# ''')

txt = """Иван, ivan@gm.com, 18 
Татьяна, tat@gm.com, 22 
Сергей, srg@ml.ru, 33 
Федор, fr@ml.ru, 41 
Елена, el@gm.com, 27"""
txt = txt.replace(',',''). replace('\n', '').split(' ')

for i in range(0,len(txt),3):
    if int(txt[i+2])< 30:
        print(f'Отправил вам сообщение {txt[i]} на почту {txt[i+1]}')
    else:
        continue
