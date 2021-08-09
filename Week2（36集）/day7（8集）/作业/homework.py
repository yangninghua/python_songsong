# 1.自定义一个数字列表，获取这个列表中的最小值
# a= [21,54,3,5,76,32]
# i =0
# min_value = a[0]
# while i <len(a):
# 	if a[i]<min_value:
# 		min_value = a[i]
# 	i+=1
# print('min=',min_value)
#----------------------------------------------------------------

# 2.自定义一个10个元素的数字列表，找出列表中最大数连同下标一起输出
# b=[32,54,23,44,12,5,87,9,12,7]
# i =0 
# max_num = b[0]
# while i<len(b):
# 	if b[i]>max_num:
# 		max_num = b[i]
# 	i+=1
# for j in range(len(b)):
# 	if b[j] == max_num:
# 		posi = j
# 		break
# print('最大数为：{}，下标为：{}'.format(max_num,posi))
#---------------------------------------------------------------------
# 3.自定义一个数字列表，求列表中第二大数的下标
# c = [21,54,3,5,76,32]
# n=0
# while n<2:
# 	i =0 
# 	max_num = c[0]
# 	while i<len(c):
# 		if c[i]>max_num:
# 			max_num = c[i]
# 		i+=1
# 	for j in range(len(c)):
# 		if c[j] == max_num:
# 			posi = j
# 			break
# 	del c[j]
# 	n+=1
# print('第二大的数为：{}，下标为：{}'.format(max_num,posi))
#-------------------------------------------------------------------

#4.B哥去参加青年歌手大奖赛,有10个评委打分，
# 去掉一个最高一个最低，求平均分
# m=[32,54,23,44,12,5,87,9,12,7]
# i = 0
# max_num = m[0]
# min_num = m[0]
# while i<len(m):
# 	if m[i]>max_num:
# 		max_num = m[i]
# 	if m[i]<min_num:
# 		min_num = m[i]
# 	i+=1
# print(max_num,min_num)
# m.remove(max_num)
# m.remove(min_num)
# aveg = sum(m)/8
# print('平均值为：%.2f' % aveg)
#-------------------------------------------------------------

# 5.定义列表，存放10个学生的成绩【成绩值0-100】，
# 获得成绩之和，平均成绩，最小成绩，最大成绩。
# grade = [82,94,63.5,74.5,62,75,87.5,90,62.5,70]
# i = 0
# max_grade = grade[0]
# min_grade = grade[0]
# while i<len(grade):
# 	if grade[i] > max_grade:
# 		max_grade = grade[i]
# 	if grade[i] < min_grade:
# 		min_grade = grade[i]
# 	i+=1
# sum_grade = sum(grade)
# aveg_grade = sum_grade/10
# print('成绩之和为：{},平均成绩为：{},最大成绩为：{},最小成绩为：{}'.format(sum_grade,aveg_grade,max_grade,min_grade))
#--------------------------------------------------------------------------

# 6.input函数每次只能输入一个字符串，请实现如下输入格式：1,20,30 。
# 然后将获得的字符串分割，得到：三个整数：1 20 30，然后求累加和。
# str_num = input('请输入数字字符串以逗号隔开：')
# b = str_num.split(',')
# print(b)
# sum = 0
# for value in b:
# 	sum+=int(value)
# print(sum)
#-----------------------------------------------------
# 7.给定一个句子（只包含字母和空格），将句子中的单词位置反转
#，单词用空格分割, 单词之间只有一个空格，前后没有空格。例如：
#  “hello xiao mi”-> “mi xiao hello”
str2 = input('请输入一个句子：')
str3_list = str2.split(' ')
str4_list = str3_list[::-1]
print(str4_list)
strr = ''
for strs in str4_list:
	if strs!='':
		strr+=strs
		strr+=' '
print(strr)