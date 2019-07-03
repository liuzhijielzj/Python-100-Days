from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)


'''
创建进程的时候，子进程复制了父进程及其所有的数据结构，
每个子进程有自己独立的内存空间，这也就意味着两个子进程中各有一个counter变量，所以结果也就可想

解决这个问题比较简单的办法是使用multiprocessing模块中的Queue类，
它是可以被多个进程共享的队列，底层是通过管道和信号量（semaphore）机制
'''
def main():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong', )).start()


if __name__ == '__main__':
    main()