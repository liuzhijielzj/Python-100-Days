from math import sqrt


def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    files = []
    try:
        for filename in filenames:
            files.append(open(filename, 'w', encoding='utf-8'))

        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    files[0].write(str(number) + '\n')
                elif number < 1000:
                    files[1].write(str(number) + '\n')
                else:
                    files[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in files:
            fs.close()
    print('操作完成!')


if __name__ == '__main__':
    main()