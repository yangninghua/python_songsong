# 死锁
'''
开发过程中使用线程，在线程间共享多个资源的时候，
如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。
尽管死锁很少发生，但一旦发生就会造成应用的停止响应，程序不做任何事情。

避免死锁：
解决：
1. 重构代码
2. 使用timeout参数

'''

from threading import Thread, Lock
import time

lockA = Lock()
lockB = Lock()


class MyThread(Thread):
    # def __init__(self,name):
    #     pass
    def run(self):  # start()
        if lockA.acquire():  # 如果可以获取到锁则返回True
            print(self.name + '获取了A锁')  #
            time.sleep(0.1)
            if lockB.acquire(timeout=5):  # 阻塞
                print(self.name + '又获取了B锁，原来还有A锁')
                lockB.release()
            lockA.release()


class MyThread1(Thread):
    def run(self):  # start()
        if lockB.acquire():  # 如果可以获取到锁则返回True
            print(self.name + '获取了B锁')
            time.sleep(0.1)
            if lockA.acquire(timeout=5):
                print(self.name + '又获取了A锁，原来还有B锁')
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread1()

    t1.start()
    t2.start()
