def main():
    f = None
    try:
        

        # 如果不愿意在finally代码块中关闭文件对象释放资源，
        # 可以使用上下文语法，通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
        #with open('致橡树.txt', 'r', encoding='utf-8') as f:
        #    print(f.read())

        # mode: r, w, x, a, +, b, t
        f = open('test.txt', 'rt', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()
        
def main2():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('致橡树.txt') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()
