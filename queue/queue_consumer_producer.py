"""
队列实现生产者消费者
"""

import queue
import time, threading

maxsize = 0
q = queue.Queue(maxsize=maxsize)

def producer(name):
    # 生产者
    count = 1
    while True:
        q.put(f'包子{count}')
        print(f'{name}现有包子{count}\n')
        count += 1
        time.sleep(2)

def consumer(name):
    # 消费者
    while True:
        print(f'{name}吃了{q.get()}\n')
        time.sleep(1)
        q.task_done()

print("======包子铺营业中========")
t1 = threading.Thread(target=producer, args=('狗不理包子铺',))
t2 = threading.Thread(target=consumer, args=('Alice',))
t3 = threading.Thread(target=consumer, args=('Bob',))

t1.start()
t2.start()
t3.start()
