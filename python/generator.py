def double_numbers(iterable):
    for i in iterable:
        yield i + 1

range_ = range(1, 900000000000)

for i in double_numbers(range_):
    print(i)
    if i >= 30:
        break;