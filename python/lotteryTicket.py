def cal_lottery_rate(a, b):
    res = a ** 5 + b ** 2
    return 1 / res

if __name__ == '__main__':
    a, b = 35, 12
    print('中奖概率：亿分之', cal_lottery_rate(35, 12) * (10 ** 8))
