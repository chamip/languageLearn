# 条件表达式两侧无括号
if 4 >= 3 > 2 and 3 != 5 == 5 != 7:
    print("关系运算符可以连续使用")
    x = None or [] or -2
    x = None
    print("&&  ||  !", "与  或  非", "and or not", sep='\n')
    print("善用 and/or 可节省行数")
    print(x)
    if not x:
        print("负数也是 True，不执行本句")
    elif x & 1:
        print("用 elif 而不是 else if\n"
        "位运算符与 C 相近，偶数&1 得 0，不执行本句")
    else:
        print("也有三目运算符") if x else print("注意结构")