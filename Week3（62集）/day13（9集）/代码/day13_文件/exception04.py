# 异常情况4
'''
# 文件操作  stream = open(...)   stream.read()   stream.close()
# 数据库操作  close()
try；
   pass
except:
   pass
finally:
   pass

'''


def func():
    stream = None
    
    try:
        stream = open(r'c:\p1\aa1.txt')
        container = stream.read()
        print(container)
        stream.close()
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('------finally-----')
        if stream:
            stream.close()
        # return 3


x = func()
print(x)
