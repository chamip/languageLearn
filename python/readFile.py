file = open("a.txt", "r", encoding="UTF-8")
#read读取文本内容以字符串返回
print(file.read())
file.close()

#readlines返回列表
print("-")
with open("a.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()
    for line in lines:
        print(line)
    file.close()

#readline逐行读取
print("--")
with open("a.txt", "r", encoding="UTF-8") as file:
    line = file.readline()
    while line != "":
        print(line)
        line = file.readline()

#with open as..自动调用close
print("---")
with open("a.txt", "r", encoding="UTF-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        line

#写文件,a模式为在文件结尾附加内容，r+支持读写
with open("b.txt", "w", encoding="UTF-8") as f:
    f.write("hello, world!\n123\n")
