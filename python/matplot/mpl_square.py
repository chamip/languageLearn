import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4 ,5]
square = [1, 4, 9, 16, 25]
plt.plot(input_values, square, linewidth=5)

plt.title('Squares', fontsize=20)
plt.xlabel('values', fontsize=15)
plt.ylabel('square of values', fontsize=15)
plt.tick_params(axis='both', labelsize=15)

plt.show()
