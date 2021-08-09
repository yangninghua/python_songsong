import os

src_path = r'c:\p1'
target_path = r'c:\p3'


def copy(src_path, target_path):  # 'c:\p1'
    # 获取文件夹里面内容
    filelist = os.listdir(src_path)  # ['a1.doc', 'aa.txt', 'girl.jpg', 'pp']   ['p1.txt','p2.txt']
    # 变量列表
    for file in filelist:
        # 拼接路径
        path = os.path.join(src_path, file)  # c:\p1\pp\p1.txt
        # 判断是文件夹还是文件
        if os.path.isdir(path):  # path = ‘c:\p1\pp’
            # 递归调用copy
            target_path1 = os.path.join(target_path, file)
            os.mkdir(target_path1)
            copy(path, target_path1)

        else:
            # 不是文件夹则直接进行复制
            with open(path, 'rb') as rstream:
                container = rstream.read()

                path1 = os.path.join(target_path, file)
                with open(path1, 'wb') as wstream:
                    wstream.write(container)
    else:
        print('复制完成！')


# 调用copy
copy(src_path, target_path)
