def ftoc():
    # print("hello,world!")
    # n = int(input("Please input an integer:"))
    # n = 2 * n;
    # print(n)
    f = float(input('请输入华氏温度：'))
    c = (f - 32) / 1.8
    print('%.2f华氏度 = %.2f摄氏度' % (f, c))
    print(f'{f:.2f}华氏度 = {c:.2f}摄氏度')

if __name__ == '__main__':
    ftoc()
