import pygal
from die import Die


die1 = Die()
die2 = Die()
results = []
for num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_val = die1.num_sides + die2.num_sides
for value in range(2, max_val + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# for i in range(1, len(results) + 1):
#     print(results[i - 1], end=' ')
#     if i % 10 == 0:
#         print()

print(frequencies)
# 对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of roll one D6 1000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
