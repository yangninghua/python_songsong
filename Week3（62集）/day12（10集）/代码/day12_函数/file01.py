# 文件操作:
'''
 文件上传
 保存log

系统函数：
 open(file,mode,buffering,encodeing)

 读:
   open（path/filename,'rt'）---->返回值：stream (管道)

   container = stream.read()  ---->读取管道中内容

   注意： 如果传递的path/filename有误，则会报错：FileNotFoundError
    如果是图片则不能使用默认的读取方式,mode = 'rb'

    总结:
    read()  读取所有内容
    readline() 每次读取一行内容
    readlines() 读取所有的行保存到列表中
    readable()  判断是否可读的

'''

stream = open(r'C:\p1\aa.txt')

# container = stream.read()
# print(container)

result = stream.readable()  # 判断是否可以读取  True  False
print(result)

# while True:
#     line = stream.readline()
#     print(line)
#     if not line:
#         break


lines = stream.readlines()  # 保存到列表中
print(lines)
for i in lines:
    print(i)

stream = open(r'C:\p1\girl.jpg', 'rb')

container = stream.read()
# print(container)
