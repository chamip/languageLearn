#!/usr/local/bin/python3.11
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

if __name__ == '__main__':
    status = http_error(1)
    print(status)

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# if __name__ == '__main__':
#     res = f(1, [])
#     print(res)
#     res = f(1, [2])
#     print(res)