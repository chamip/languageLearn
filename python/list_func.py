#list列表pop()方法，list.pop([i]),默认删除最后一个元素并返回
def list_test():
    print('---list_test()---')
    l = [1, 2, 3]
    l.pop()
    print(l)
    a = l.pop()
    print(a, "...", l)

from collections import deque
#用列表实现队列效率低，使用deque
def deque_imple_queue():
    print('---deque_imple_queue()---')
    queue = deque(['aaa', 'bbb', 'ccc'])
    queue.append('ddd')
    queue.append('eee')
    print(queue)
    queue.popleft()
    print(queue)

# from math import pi
if __name__ == '__main__':
    list_test()
    deque_imple_queue()
    # ls = [round(pi, i) for i in range(1, 6)]
    # print(ls)