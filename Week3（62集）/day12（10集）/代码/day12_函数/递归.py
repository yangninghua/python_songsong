# 递归
# 入口 1   出口  10

def sum(n):
    if n == 10:
        return 10
    else:
        return n + sum(n + 1)


result = sum(1)

print(result)