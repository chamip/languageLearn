import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 获取最高温度和日期
filename = 'Beijing_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    for index, column_reader in enumerate(header_row):
        print(index, column_reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
    print(dates)
    print(highs)
    print(lows)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128)
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # 填充两个y值系列中间的空间
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # 设置图形的格式
    plt.title('Daily Temperatures 2014 Beijing', fontsize=20)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)', fontsize=12)
    plt.tick_params(axis='both', labelsize=12)
    plt.show()
