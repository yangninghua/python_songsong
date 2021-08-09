# 1 写出一段Python代码实现删除一个list里面的重复元素
# import random
# li = []
# for i in range(10):
#     ran = random.randint(1,10)
#     li.append(ran)
# print(li)
#
# for i in li:
#     if li.count(i) >= 2:
#         li.remove(i)
# print(li)


# 2 键盘输入多个人名保存到一个列表中，如果里面有重复的则提示此姓名已经存在
# names = []
# while True:
#     name = input("输入名字")
#     if name not in names:
#         names.append(name)
#         print('添加成功',names)
#     else:
#         print('此姓名已经存在')


# 3 Python中pass语句的作用是什么（面试题）

# 占位，不执行任何操作



# 4.两个列表[1,5,7,9]和[2,2,6,8]合并并排序 结果为:[1,2,2,3,6,7,8,9]
# li1 = [1,5,7,9]
# li2 = [2,2,6,8]
# li3 = li1 + li2
# for i in range(len(li3)-1):
#     for j in range(len(li3)-i-1):
#         if li3[j] > li3[j+1]:
#             li3[j],li3[j+1] = li3[j+1],li3[j]
# print(li3)




# 5.[[6,2],[8,4,2],[5,6,1]] 转存到一个新的列表中并排序。结果为[1,2,3,4,5,6,6,8]
# li = [[6,2],[8,4,2],[5,6,1]]
# new_li = []
# for i in li:
#     for j in i:
#         new_li.append(j)
#         for a in range(len(new_li)):
#             for b in range(a+1,len(new_li)):
#                 if new_li[a] >new_li[b]:
#                     new_li[a],new_li[b] = new_li[b],new_li[a]
# print(new_li)


# (1)
score = []

# (2)
li = ('68','87','92','100','76','88','54','89','76','61')
for i in li:
    score.append(int(i))
print(score)

# (3)
print(score[2])

# (4)
print(score[0:5])

# (5)
score.insert(2,59)
print(score)

# (6)
num = 76
print(score.count(num))

# (7)
if num in score:
    print('有考试成绩')

# (8)
print(score.index(100))

# (9)
for i in range(len(score)):
    if score[i] == 59:
        score[i] += 1
print(score)


# (10)
del score[0]
print(score)

# (11)
len(score)

# (12)
score.sort(reverse=False)
print(score[0])
print(score[-1])

# (13)
score.reverse()
print(score)

# (14)
print(score.pop())

# (15)
score.append(88)
score.remove(88)
print(score)

# (16)
score1 = [80,61]
score2 = [71,95,82]
print(score1+score2)

# (17)
for i in range(5):
    for j in score1:
        score2.append(j)
print(score2)