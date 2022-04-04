
# def myABS(x):
#     x = -x if (x<0) else x
#     return x
# print(myABS(-4))

# def isPositive(x):
#     return x>=0
#
# p = []
# for i in range(-4,10):
#     if isPositive(i):
#         p.append(i)
# print(p)

# def max2(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# def max3(a,b,c):
#     return max2(a, max2(b,c))
# print(max2(-3,30))
# print(max3(3,90,5))

# def plochad(a,b):
#     return a*b
# print(plochad(10,23))

def sum1(a):
    sum =0
    for i in a:
        sum +=i
    return(sum)

a = [1,2,3,4,5,6,7,8,9]
print(sum1(a))