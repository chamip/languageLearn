import matplotlib.pyplot as plt
from random_walk import RandomWalk

# index = 0
# 创建RandomWalk示例，绘制随机漫步
while True:
    # index += 1
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    # plt.figure(figsize=(10, 6))

    point_nums = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_nums, cmap=plt.cm.Blues, edgecolors='none', s=1)
    # save_name = f'rw{index}.png'

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()
    # plt.savefig(save_name, bbox_inches='tight')

    keep_running = input('Make another walk?(y/n):')
    if keep_running == 'n':
        break
