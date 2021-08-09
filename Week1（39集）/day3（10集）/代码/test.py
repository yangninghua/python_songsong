print('*' * 50)

print('\t 英雄联盟')
 
print('*' * 50)


name='jack'

name1='jack'

name2='jack1'

print(id(name))
print(id(name1))
print(id(name2))


print(bin(-128)) 



'''
4字节 -32bit 
8字节 -64bit
1

0000 0000 0000 0000 0000 0000 1000 0000
-128

1 000 0000 0000 0000 0000 0000 1000 0000

1 111 1111 1111 1111 1111 1111 0111 1111

1 111 1111 1111 1111 1111 1111 1000 0000
'''
print(bin(128))

import sys
print(sys.maxsize)

print(sys.getsizeof(int()))

x=12
print(2<x<10)

print(++x > 10)
print(x)

a= 4 
b=5
c=8
a-=1

res= (a>(a-=1)+c)  and (c++<(b-=1)+(a+=1))

print(res)