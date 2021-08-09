# 语法错误和异常
# 语法错误：
# while True:
#     print('-------')

# number = 100
#
#
# def func():
#     global number
#     number += 1


# 异常：程序运行的时候报出来的。xxxError
# def chu(a, b):
#     return a / b
#
#
# x = chu(4, 2)  # ZeroDivisionError: division by zero
# print('--------------->', x)

# 异常处理:
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
  except 异常的类型1：
        print（。。。。）
  except 异常类型2:
       pass

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

        print('结果是:', sum)
    except ZeroDivisionError:
        print('除数不能为零！！！！')
    except ValueError:
        print('必须输入数字！！！！')
    except FileNotFoundError:
        pass
    except NameError:
        pass
    except Exception:
        pass

func()

print('------------>')
