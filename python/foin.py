import random
from math import sqrt

def foin():
    sum = 0
    for x in range(1, 100 + 1):
        sum += x
    print('sum = ', sum)
    sum1 = 0
    for x in range(1, 100, 3):
        sum1 += x
    print(f'sum1 = {sum1:d}')
    sum2 = 0
    for x in range(100, 0, -2):
        sum2 += x
    print('sum2 = %d' % sum2)
    sum3 = 0
    for x in range(99, 1, -1):
        sum3 += x
    print('sum3 = ', sum3)

def guess():
    answer = random.randint(1, 100)
    count = 0
    while True:
        count += 1
        number = int(input('请输入猜测数字：'))
        if number == answer:
            print('恭喜你猜对了！')
            break
        elif number < answer:
            print('数字猜小了.')
        else:
            print('数字猜大了.')
    print('你一共猜测了%d次.' % count)
    if count > 7:
        print('你的智商已下线qwq.')

def multi_loop():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d * %d = %d' % (i, j, i * j), end = '\t')
        print()

def isPrime():
    number = int(input('请输入一个数：'))
    end = int(sqrt(number))
    flag = True
    for x in range(2, end + 1):
        if (number % x == 0):
            flag = False
            break
    if flag and number != 1:
        print(f'{number:d}是素数.')
    else:
        print(f'{number:d}不是素数.')

def gcdLcm():
    x = int(input('请输入x：'))
    y = int(input('请输入y：'))
    if x > y:
        x, y = y, x
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            print(f'{x:d}和{y:d}的最大公约数是：{i}')
            print(f'{x:d}和{y:d}的最小公倍数是：{x * y // i}')
            break

def printTriangle():
    row = int(input('请输入行数：'))
    for i in range(row):
        for j in range(i + 1):
            print('*', end = '')
        print()
    '''
    for i in range(row):
        for j in range(row - i - 1):
            print(' ', end = '')
        for j in range(i + 1):
            print('*', end = '')
        print()
    '''
    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end = '')
            else:
                print('*', end = '')
        print()

    for i in range(row):
        for j in range(row - i - 1):
            print(' ', end = '')
        for j in range(2 * i + 1):
            print('*', end = '')
        print()

def add(*args):
    total = 0
    for x in args:
        total += x
    return total

if __name__ == '__main__':
    foin()
    # guess()
    multi_loop()
    # isPrime()
    # gcdLcm()
    # printTriangle()
    print(add())
    print(add(1, 2, 3))
    print(add(1, 2, 3, 4, 5, 10))
