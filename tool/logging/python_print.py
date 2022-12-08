from random import random
from time import sleep
from threading import Thread
"""
print若要安全输出，需要加锁。否则线程不安全，因为线程是上下文切换的。
"""

# task for worker threads
def task(number):
    # generate random number between 0 and 1
    value = random()
    # block
    sleep(value)
    # report
    print(f'Thread {number} got {value}.')

# start the threads
threads = [Thread(target=task, args=(i,)) for i in range(100)]

# start threads
for thread in threads:
    thread.start()
# wait for threads to finish
for thread in threads:
    thread.join()

# 结果是 1,000 条消息同时打印到标准输出。