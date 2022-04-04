# p = ("+7923456781", "+7923454782", "+7923556783", "+5923456784", "+3923456785", "+7923456556")
#
# p = list(p)
# for i in p:
#     if '+7' in i:
#         print(i)
#     else:
#         continue


# txt = "Оценки: 5, 4, 3, 4, 2, 4, 5, 4"
# a = ()
# for i in txt:
#     if i.isdigit():
#         a += (int(i),)
#     else:
#         continue
# print(a)

txt = ((1,2,3),(3,4,5),(6,7,8))
for i in range(len(txt)):
    print('\t')
    for j in range(len(txt[i])):
        print((txt[i][j]),end=' ')
