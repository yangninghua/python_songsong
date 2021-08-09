# 

if 'good'=='good':   # == 比较的是内容 'good'  'good'
	print('相等')

if 'good' in 'goods':  # in   运算符  应用在字符串判断中  也可以用在[]
	print('相等或者包含')


i=1

for w in ['goods','good','abc','aaaa']:
	# w=goods   w=good   w=abc    w=aaaa
	print('good' in w)   # True    True    False   False 
	print('------->',i)
	i+=1


# A. 1   B,2   C.1,2  D: 以上都对


if 'good' in ['goods','good','abc','aaaa']:
	pass


'''
 if 让 in 判断作为一个条件表达式：
   if 'a' in 'abc':
   	pass

   if 'a' in ['a','b','c']:
   	 pass

 但是：
 for ... in    循环条件  

 for 变量  in 字符串|列表:
 	pass



'''


'''


'''

a=6
b=9

# temp = a  # temp =6
# a = b
# b = temp

# print(a,b)
# a,b=0,1
a,b=b,a
print(a,b)