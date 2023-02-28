def double_numbers(genetators):
    for i in genetators:
        yield i + i

range_ = range(1, 90000000)
for i in double_numbers(range_):
    print(i)
    if i >= 30:
        break
