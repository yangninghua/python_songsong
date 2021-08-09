def func(a, b):
    c = 9

    def inner_func():
        s = a + b + c
        print(s)

    return inner_func


f1 = func(1, 2)   # f1 = inner_func  001  1,2
print(f1)
f1()

f1()

f1()

#
f2 =  func(3, 4)  # 002 3,4   f2 = inner_func
f2()
#
# func(1, 2)


f3 = func(1,2)
print(f3)