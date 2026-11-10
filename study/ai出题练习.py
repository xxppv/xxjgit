#11.10继续复习基础
#for循环
#for i in range(1,11):
#    print(i)
#sum = 0
#for i in range(1,101):
#    sum += i
#    i +=1
#    print(sum)
#for i in range(1,21):
#    if i % 2 == 0:
#        print(i)
#while循环
#i = 1
#while i <=5:
#    print(i)
#    i=i+1
#sum = 0
#while True:
#    a = int(input('请输入数字:'))
#    if a == 0:
#        break
#   sum = sum + a
#print(sum)
#列表基础:
nums = [12,45,7,23,89]
print(len(nums))
print(max(nums))
print(min(nums))
fruit = ['苹果','香蕉','橘子','葡萄']
for i in fruit:
    print(i)
for i in range (1,5):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
#11.9复习前面的基础
#1.打印与变量
#print('hello python')
#b = 3
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)

#name = 'lucky'
#print('我的名字是：',name)
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
#for i in range(1,6):
#   for j in range(1,i+1):
#        print('*',end='')
#    print()