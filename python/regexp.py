import re
pat = re.compile('(x+x+)+y')

from time import process_time as now

for n in range(10, 100):
    print(n)
    start = now()
    pat.search('x' * n + 'y')
    print(now() - start, end=' ')
    start = now()
    pat.search('x' * n)
    print(now() - start)
