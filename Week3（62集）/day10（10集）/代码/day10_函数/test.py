# s = {1, 3, 5, 7, 8, 9}
#
# for i in s:
#     print(i)
#
# for index, i in enumerate(s):
#     print(index, i)
#
# print(enumerate(s))
#
#
# list1 = []
# index=0
# for i in s:
#     t1 = (index,i)
#     list1.append(t1)
#
#     index+=1
#
# print(list1)
#
# print('--------------------------')
# for index,value in list1:
#     print(index,value)


# 复用

# def enumerate(value):
#     list1 = []
#     index = 0
#     for i in value:
#         t1 = (index, i)
#         list1.append(t1)
#
#         index += 1
#     print(list1)
#
#
# s = {2, 5, 7, 9, 0, 7}
# enumerate(s)


list1 = [1,3,5,8,9,0]

list2 =list1

list1.remove(5)

print(list2)


s='abc'

s1=s

s= 'abcd'

print(s1)