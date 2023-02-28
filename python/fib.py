def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return [a]

def fib_yield(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

def main():
    for i, val in  enumerate(fib(5)):
        print(i, " : ", val)
    print()
    for val in fib_yield(5):
        print(i, " : ", val)

if __name__ == '__main__':
    main()
