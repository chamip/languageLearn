class class_object(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能看<熊出没>' % self.name)
        else:
            print('%s可以看大型电影.' % self.name)

if __name__ == '__main__':
    name = input('请输入姓名：')
    age = int(input('请输入年龄：'))
    co1 = class_object(name, age)
    co1.study('Python')
    co1.watch_movie()
