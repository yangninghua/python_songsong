'''
变量
运算符



语句：
条件判断语句
循环语句
跳转语句

条件语句:（判断）
应用场景：
1. 用户名和密码登录
2. 用户登录验证（看影院信息，判断用户是否登录了，没有登录弹窗口，登录看到信息）
  
  
if 条件：
   条件成立执行的语句


'''

username='admin'  # 没有登录
# password=''
# python: 判断的变量是''  0  None 默认是False
# python： 如果变量有值'abc','kkkk','yueryu',认为是True   

if username:  # 'admin'!=''  True   如果条件运算结果是True则进入内层
	print('嘿嘿！我登录啦！')

print('-------------')


num =9 

if num:
	print('------>',num)



'''
if num:
	print('.....')

等效:

if num!=0:
	print('.....')

'''

'''
练习:
如果年龄大于18  并且  输入le姓名，则打印xxx今年xxx岁

'''

# age = int(input('输入年龄:'))
# username=input('输入用户名')

# if age>18 and  username:  # True and False --->False
# 	print('{}今年{}岁了!'.format(username,age))


# print('---game over----')


'''
if 判断的第二种使用方式:

if 表达式(条件):
	条件成立
else:
	条件不成立执行的语句

注意：添加缩进  一个tab

'''

'''
需求:
  消消乐
    lv1
    lv2
 

  lv1:  免费玩 随便玩

  lv2:  充值  买道具  继续玩


'''

# print('*'*10,'欢迎来到消消乐','*'*10)
# level = input('请输入你的级别（lv1，lv2）:')
# if level=='lv1':
# 	print('免费玩 随便玩')
# else:
# 	print('已经进入付费级别，充值继续玩')
# 	money = int(input('请充值(必须是100的倍数):'))
# 	# if 语句是允许嵌套，注意缩进问题
# 	if money%100==0 and money>0:
# 		print('充值成功！充值金额是:',money)
# 	else:
# 		print('充值失败，充值金额必须是100的倍数！')


'''
 if 条件1:
 	 成立
 	 if 条件2:
 	 	 成立
	 else:
	 	 不成立
 else:
 	 不成立
 	 if 条件3:
 	 	 成立
	 else:
	 	 不成立

'''
# 随机数：
import random

# print(random.randint(1,10))

'''
猜大小

步骤：
1. 系统产生一个随机数
2. 键盘输入一个数
3. 将系统产生的与键盘输入的进行比较
4. 猜对了，中大奖  猜错啦  拜拜下次再来

'''
# ran = str(random.randint(1,10))   # 8
# num =input('请输入(1-10)之间的随机:')  # '8'


# # print(8 =='8')
# if ran == num:
# 	print('恭喜中大奖啦！奖品是：笔记本')
# else:
# 	print('很遗憾你猜错啦！与奖品擦肩而过~~~')


'''

多层条件判断:
if 100-90:
	优+
elif 90-80
    优-
elif  80-70
    良
elif  70-60
   及格
else
   不及格


'''

age = int(input('请猜猜宋宋姐年龄:'))

if age <= 18 and age>0:
	print('(o゜▽゜)o☆[BINGO!] 太有眼光啦！')
elif age>18 and age<=30:
	print('人家还是宝宝呢.....')
elif age>30 and age<=40:
	print('长得太年轻了吧!!!!')
else:
	print('输入错误！')


'''
4种:

if 条件:
	  语句

----------
if 条件:
	语句
else:
	语句

----------

if 条件1:
	.....
	if 条件2:
		语句
	else:
		语句
else:
	.....

-----------
if 条件1：
     语句
elif 条件2:
	语句
elif 条件3:
	....
else:
	语句



'''