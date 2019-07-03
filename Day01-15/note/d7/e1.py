import os
import time

def main():
    content = '长沙欢迎你！为你开天辟地......'
    while True:
        os.system('cls') # os.system('clear')
        print(content)
        time.sleep(0.2) # ms
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()