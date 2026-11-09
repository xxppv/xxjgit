#11.9复习前面的基础
#1.打印与变量
print('hello python')
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)

name = 'lucky'
print('我的名字是：',name)
#复习条件判断
#n = input('请输入一个数字：')
#if n == '0':
#    print(n,'是0')
#elif n > '0':
#    print(n,'是一个正数:')
#elif n < '0':
#    print(n,'是一个负数')

#a = input('请输入一个年龄:')
#if a >= '18':
#   print('成年人')
#elif a<= '18':
#    print('未成年')
#判断是否为闰年
#y = int(input('请输入一个年份:'))
#if y % 400 == 0:
#    print(y,'是闰年')
#elif y % 4 == 0 and y % 100 != 0:
#    print(y,'是闰年')
#循环的复习
#for i in range(1,101):
#    print(i)
#sum = 0
#for i in range(1,101):
#    sum += i
#    print(sum)
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()