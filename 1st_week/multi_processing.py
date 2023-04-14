from multiprocessing import Process
import os

# 프로세스 만들기
# print('hello, os')

# print('hello, os')
# print('my pid is', os.getpid())


# 멀티 프로세싱
def foo():
    print('child process', os.getpid())
    print('my parent is', os.getppid())

# if __name__ == '__main__':
#     print('parent process', os.getpid())
#     child = Process(target=foo).start()


def bar():
    print('hello, os')

# if __name__ == '__main__':
#     child1 = Process(target=bar).start()
#     child2 = Process(target=bar).start()
#     child3 = Process(target=bar).start()


def gab():
    print('this is gab')


def eul():
    print('this is eul')


def byeong():
    print('this is byeong')


if __name__ == '__main__':
    print('parent process', os.getpid())
    child0 = Process(target=foo).start()
    child00 = Process(target=bar).start()
    child1 = Process(target=gab).start()
    child2 = Process(target=eul).start()
    child3 = Process(target=byeong).start()