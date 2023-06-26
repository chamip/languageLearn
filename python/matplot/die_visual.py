import pygal
from die import Die


die = Die()
results = []
for num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides + 1):
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
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
