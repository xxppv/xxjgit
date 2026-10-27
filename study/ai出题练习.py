#10.27的题目练习
#1.先拟定好一个秘密数字，让用户输入数字猜
#secret = 8
#while True:
#    i = int(input("请输入数字："))
#    if i > secret:
#        print(f"猜大了")
#    if i < secret:
#        print(f"猜小了")
#    if i == secret:
#        print(f"答对了！")
#        break
#总结：虽然是一个很基础的问题，但是我的脑子不会转弯，也是一直做不对，虽然知道要用while，if.else，这些但是对于是里面还是外面就是分不清楚，通过这个小题练习已经懂了
#2.从5开始倒计时
from contextlib import nullcontext

i = 5
while i <= 5:
    print(i)
    if i == 0:
        break
    i = i-1
print("出发！")
#3.找字母t,跳过
word = 'python'
for char in word:
    if char == 't':
        print("跳过")
        continue
    print(char)
#总结：在跳过这里花费了不少时间，因为没有弄清除continue的原理，缩进也有问题
#4.跳过偶数
for i in range(1,11):
    if i % 2 == 0:
        print("跳过")
        continue
    print(i)
#5.计算1加到100的和
i = 1
s = 0
while i <= 100:
    s = s + i
    i = i + 1
    print(s)