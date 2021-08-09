'''
格式:
try:
    可能出现异常的代码
except:
    如果有异常执行的代码
[finally:
    无论是否存在异常都会被执行的代码]


情况1：
  try:
     有可能会产生多种异常
  except 异常类型1：
        print（。。。。）
  except 异常类型2:
       pass
  except Exception:
       pass

  如果是多个except，异常类型的顺序需要注意，最大的Exception要放到最后



情况2：获取Exception的错误原因
try:
     有可能会产生多种异常
  except 异常类型1：
        print（。。。。）
  except 异常类型2:
       pass
  except Exception as err:
       print(err)  ----> err的内容就是错误原因：

   pop from empty list  ---》 从空的列表中删除内容
   。。。

'''


def func():
    try:
        n1 = int(input('输入第一个数字:'))
        n2 = int(input('输入第二个数字:'))
        # + 加法
        per = input('输入运算符号(+ - * /):')

        result = 0
        if per == '+':
            result = n1 + n2
        elif per == '-':
            result = n1 - n2
        elif per == '*':
            result = n1 * n2
        elif per == '/':
            result = n1 / n2
        else:
            print('符号输入有误！')

        print('结果是:', result)

        # 操作列表
        list1 = []
        list1.pop()  #

        # 文件操作
        with open(r'c:\p1\aa.txt', 'r') as  wstream:
            print(wstream.read())

    except ZeroDivisionError:
        print('除数不能为零！！！！')
    except ValueError:
        print('必须输入数字！！！！')
    except Exception as err:
        print('出错啦！', err)


func()

print('------------>')
