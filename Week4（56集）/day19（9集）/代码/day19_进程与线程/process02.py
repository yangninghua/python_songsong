'''
生活中，你可能一边听歌，一边写作业；一边上网，一边吃饭。。。这些都是生活中的多任务场景。电脑也可以执行多任务，比如你可以同时打开浏览器上网，听音乐，打开pycharm编写代码...。简单的说**多任务就是同一时间内运行多个程序**

- 单核CPU实现多任务原理：操作系统轮流让各个任务交替执行，QQ执行2us，切换到微信，在执行2us，再切换到陌陌，执行2us……。表面是看，每个任务反复执行下去，但是CPU调度执行速度太快了，导致我们感觉就行所有任务都在同时执行一样

- 多核CPU实现多任务原理：真正的秉性执行多任务只能在多核CPU上实现，但是由于任务数量远远多于CPU的核心数量，所以，操作西永也会自动把很多任务轮流调度到每个核心上执行

- 并发和并行
  - **并发**：当有多个线程在操作时,如果系统只有一个CPU,则它根本不可能真正同时进行一个以上的线程，它只能把CPU运行时间划分成若干个时间段,再将时间 段分配给各个线程执行，在一个时间段的线程代码运行时，其它线程处于挂起状。.这种方式我们称之为并发(Concurrent)。
  - **并行**：当系统有一个以上CPU时,则线程的操作有可能非并发。当一个CPU执行一个线程时，另一个CPU可以执行另一个线程，两个线程互不抢占CPU资源，可以同时进行，这种方式我们称之为并行(Parallel)。
- 实现多任务的方式：
  - 多进程模式；
  - 多线程模式；
  - 协程。
  进程  >  线程  >  协程

  from multiprocessing import Process

  process = Process(target= 函数，name=进程的名字，args=（给函数传递的参数）)
  process 对象

  对象调用方法:
  process.start()    启动进程并执行任务
  process.run()  只是执行了任务但是没有启动进程
  terminate()   终止
'''

# 进程创建
import os
from multiprocessing import Process
from time import sleep


def task1(s, name):
    while True:
        sleep(s)
        print('这是任务1.。。。。。。。。。。', os.getpid(), '------', os.getppid(), name)


def task2(s, name):
    while True:
        sleep(s)
        print('这是任务2.。。。。。。。。。。', os.getpid(), '------', os.getppid(), name)


number = 1
if __name__ == '__main__':
    print(os.getpid())
    # 子进程
    p = Process(target=task1, name='任务1', args=(1, 'aa'))
    p.start()
    print(p.name)
    p1 = Process(target=task2, name='任务2', args=(2, 'bb'))
    p1.start()
    print(p1.name)

    while True:
        number += 1
        sleep(0.2)
        if number == 100:
            p.terminate()
            p1.terminate()
            break
        else:
            print('---------------->number:',number)

    print('--------------')
    print('*****************')
