'''

  循环导入：大型的python项目中，需要很多python文件，由于架构不当，可能会出现模块之间的相互导入
   A：模块
     def test():
        f()
   B: 模块
     def f（）：
        test()

  避免产生循环导入：
  1. 重新架构
  2. 将导入的语句放到函数里面
  3. 把导入语句放到模块的最后
'''
from 循环导入2 import func


def task1():
    print('-------task1-------')


def task2():
    print('--------task2---------')
    func()


#
if __name__ == '__main__':
    # 调用task1
    task1()
    task2()
