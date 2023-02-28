import os
import time

def pmd():
    content = 'hello,world!'
    while True:
        os.system('cls')
        print(content)
        time.sleep(1.0)
        content = content[1:] + content[0]

if __name__ == '__main__':
    pmd()
