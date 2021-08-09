# 定义类和属性
class Student:
    # 类属性
    name = 'xiaowei'
    age = 2


xiaowei = Student()

# print(xiaowei.gender)  # AttributeError: 'Student' object has no attribute 'gender'

xiaowei.age = 18

print(xiaowei.age)
print(xiaowei.name)

yupeng = Student()
print(yupeng.name)

yupeng.name = 'xiaopengpeng'

print(yupeng.name)
print(yupeng.age)

yupeng.age = 1
print(yupeng.age)

print(xiaowei.age)

Student.name = 'feifei'

ruirui = Student()
print(ruirui.name)
