# 异常
'''
 情况3：try...except..(多个except)...else
  try:
     有可能有异常的代码
  except 类型1:
      pass
      ..
  else:
     如果try中没有发生异常则进入的代码

注意： 如果使用else则在try代码中不能出现return
'''


def func():
    try:
        n1 = int(input('输入数字:'))
        print(n1)
        return 1
    except ValueError:
        print('必须是数字....')
        return 2
    else:
        print('数字输入完毕！')   # 没有异常才会执行的代码块


# 调用函数
func()