import threading
import os

# print('process id', os.getpid())
#
#
# def foo():
#     print('tread id', threading.get_native_id())
#     print('process id', os.getpid())
#
#
# if __name__ == '__main__':
#     print('process id', os.getpid())
#     thread1 = threading.Thread(target=foo).start()
#     thread2 = threading.Thread(target=foo).start()
#     thread3 = threading.Thread(target=foo).start()


# 각기 다른 작업을 하는 스레드 생성하기
def foo():
    print('This is foo')


def bar():
    print('This is bar')


def baz():
    print('This is baz')

if __name__ == '__main__':
    print('process id', os.getpid())
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()

