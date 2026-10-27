print('hello world')
print('123')
print(9)
print('hhhhh','嘻嘻嘻')
print('hello',end=' ')
print("你好")
num1 = 5
num2 = 6
total = num1+num2
print(total)
a = 888
a = 8888
print(a)
A = 653
print(A)
num = 5000
print(type(num))
num1 = 1.1
print(type(num1))
print(type(1+4j))
name = 'six'
print(type(name))
print(name)
#占位符 %s  在输出的时候引号外也得有一个%
name = 'xx'
print("我的名字:%s" % name)
a = 1.569887
print("%f" % a)
a =1.7894563
print("%f" % a)
print("%.3f" % a)
#格式化 f"{表达式}"
name = "xx"
age = 88
print(f"姓名{name},年龄{age}")
#算数运算符练习 //取整数，%取余数，**幂（a ** b：a的b次方）
a = 6
b = 3
print(a // b)
print(a % b)
print(a ** b)
print(a ** b // b + a)
#赋值运算
a1 = 50
b1 = 60
a2 = a1 +b1
print(a2)
#n +=10(n+10=n) n -=也是一个道理
n = 5
n +=10
print(n)
n -= 45
print(n)
#input()输入函数
#prompt是提示，会在控制台显示
##print(name)
#if基础语句练习
age = 18
if age >= 18:
    print("可以上网")
score = input("输入成绩:") #默认是int，所以数字也是字符串，需要打上引号，否则就会报错
if score >= '60':
    print("已及格")

