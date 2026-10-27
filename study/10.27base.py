#score = input("输入成绩:")
#if '70'>=score >= '60':
#    print("及格")
#if '70'<=score<='90':
#    print("良好")
#if '90'<=score<='100':
#    print("优秀")
#else:
#    print("不及格")
#while循环
i = 1
while i<=4:
    print("加油，彭小宁，你是最棒的！")
    i +=1
i = 1
s = 0
while i<=5:
    s = s + i
    i += 1
    print("计算结果:",s)
i = 1
while i<=3:
    print(f"这是{i}次外循环")
    j = 1
    while j<=4:
        print(f"这是{j}次内循环")
        j += 1
    i = i + 1
#for循环
for i in range(1,5):
    print(i)
s = 0
for i in range(1,101):
    s = s + i
    print("计算结果:",s)
#break
i = 1
while i <=5:
    print(f"小彭在吃第{i}个苹果")
    if i == 3:
        print("吃饱了不吃了")
        break
    i = i + 1
#continue
while i <=5:
    print(f"小彭在吃第{i}个苹果")
    if i == 3:
        print(f"吃到了虫子，第{i}个苹果不吃了")
        i = i + 1
        continue     #在continue之前不改变计数，就会死循环
    i = i + 1
print("好好学习，天天向上"*3)
print("好好学习，天天向上\n"*3)
name = '小彭'
print('小' in name)
print('徐' in name)
print('彭' not in name)
name = 'lucky'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[-1])
print(name[-2])
s = 'abcdefg'
print(s[2:5])
print(s[3:])
print(s[2:])
print(s[-1:])
print(s[::-1])
print(s[::-2])
print(s[1::])
print(s[0::])    #牢记从0开始（下标）

