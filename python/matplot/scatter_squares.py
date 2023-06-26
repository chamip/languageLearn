import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=20)
plt.title('Square', fontsize=15)
plt.xlabel('x', fontsize=10)
plt.ylabel('y', fontsize=10)
plt.tick_params(axis='both', labelsize=10)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
plt.show()
# 保存为图片
# plt.savefig('square_plot.png', bbox_inches='tight')
