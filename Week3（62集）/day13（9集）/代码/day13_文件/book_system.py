# 持久化保存：文件
# list 元组，字典---->内存

# 用户注册
def register():
    username = input('输入用户名:')
    password = input('输入密码:')
    repassword = input('输入确认密码:')

    if password == repassword:
        # 保存信息
        with open(r'c:\p1\book\users.txt', 'a') as wstream:
            wstream.write('{} {}\n'.format(username, password))

        print('用户注册成功！')
    else:
        print('密码不一致！')


# 用户登录
def login():
    username = input('输入用户名:')
    password = input('输入密码:')

    if username and password:
        # 打开文件查看
        with open(r'c:\p1\book\users.txt')  as rstream:
            # 逐行读取内容
            while True:
                # 读取一行内容
                user = rstream.readline()  # admin 123456\n
                # 判断有没有读取到内容
                if not user:
                    print('用户名或者密码输入有误！')
                    break
                # 构造比较格式
                input_user = '{} {}\n'.format(username, password)
                # 如果用户输入的跟文件中的内容一致则认为用户登录成功
                if user == input_user:
                    print('用户登录成功！')
                    break


def show_books():
    print('---------图书馆里面的图书有:----------')
    with open(r'c:\p1\book\books.txt', 'r') as rstream:
        books = rstream.readlines()
        for book in books:
            print(book, end='')  # 因为读取的内容中有\n 所以取消print中自带的末尾换行

# 调用函数:
# register()
# login()
# show_books()
