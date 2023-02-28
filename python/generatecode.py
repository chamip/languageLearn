import random
def generate_code(code_len = 4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, length)
        code += all_chars[index]
    return code

if __name__ == '__main__':
    code = generate_code(5)
    print('generated code is:', code)
