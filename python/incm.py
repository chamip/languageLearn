def inchcentmeter():
    value = float(input('请输入长度：'))
    unit = input('请输入单位（in/cm/英寸/厘米）：')
    if unit == 'in' or unit == '英寸':
        print('%.1f inch = %.1f centmeter.' % (value, value * 2.54))
    elif unit == 'cm' or unit == '厘米':
        print(f'{value:.2f} centmeter = {value / 2.54 : .2f} inch')
    else:
        print('请输入正确单位.')

if __name__ == '__main__':
    inchcentmeter()
