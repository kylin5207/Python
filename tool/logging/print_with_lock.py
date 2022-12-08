"""
可以使用上下文管理器接口将对print()的调用更新为受锁保护。
"""

# SuperFastPython.com
# example of thread-safe print
from random import random
from time import sleep
from threading import Thread
from threading import Lock


# task for worker threads
def task(number, lock):
    # generate random number between 0 and 1
    value = random()
    # block
    sleep(value)
    # report
    with lock:
        print(f'Thread {number} got {value}.')


# create a shared lock
lock = Lock()
# configure many threads
# 然后我们可以在配置时将锁作为参数传递给每个线程。
threads = [Thread(target=task, args=(i, lock)) for i in range(1000)]
# start threads
for thread in threads:
    thread.start()
# wait for threads to finish
for thread in threads:
    thread.join()
