# a = 0b00101000
# print(int(a))

# b= 0o00002171

# print(int(b))

# c= 0x00005AFB
# print(int(c))

# a,b=2,4
# b=c=5

# print(c-a>b-a)

# a+=3

# result = a+b

# print(result)


# t = int(input('输入天气温度:'))

# if t>30:
# 	print('太热了')
# else:
# 	print('还行！')

# 使用while循环实现输出1-50之间偶数 的和
# sum = 0
# i = 1 

# while i<=50:
# 	# print(i)
# 	if i%2==0:
# 		sum +=i

# 	i+=1

# print('sum=',sum)



# 补充:
# sum=0
# for i in range(1,51):  # 0~49	
# 	# b=0
# 	# b+=i
# 	# sum =0

# 	if i%2==0:
# 		sum+=i

# print('sum=',sum)
# print('完成for循环之后i的值是:',i)
# print('b====>',b)


'''
目的：
 1.声明变量的位置：声明在for，while的外层，sum+=i  相当于累加，如果放在for，while循环的内层
 相当于每次循环都会执行sum=0

 2. python 在for，while循环中没有变量的作用域。 在for，while循环结构的外层都可以获取值


'''


'''
break,continue 跳转语句:


'''
# 方式一:

sum = 0 
for i in range(10):
	if i%3!=0:
		sum+=i
print('sum-----1111->',sum)


# 方式二:

sum =0 

for i in range(10):  # 0~9
# 任务1
	if i%3==0:
		#  pass  break  continue
		# break   # 跳出整个for循环结构
		continue  # 跳过循环体中下方的语句不执行，直接进行下一次的循环
# 任务2
	sum+=i

print('sum-----2222->',sum)