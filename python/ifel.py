def ifelse():
    # print("hello,world!")
    # n = int(input("Please input an integer:"))
    # n = 2 * n;
    # print(n)
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == 'admin' and password == '123456':
        print('验证成功！')
    else:
        print('验证失败。')

if __name__ == '__main__':
    ifelse()
