# Queue模块

​	queue模块实现了多生产者、多消费者队列。这特别适用于消息必须安全地在多线程交换的线程编程。

​	该模块实现了三种类型的队列，它们的区别是任务取回的顺序。

- 在FIFO队列中，先添加任务的先取回。
- 在LIFO队列中，最后添加的任务先取回（该操作类似于堆栈）。
- 在优先级队列中，条目将保持排序（使用heapq模块）并且最小值的任务第一个返回。

## 一、使用

### 创建

```python
import queue

q = queue.Queue(maxsize=5)
```

​	`queue.Queue(maxsize=xxx)`创建队列，maxsize是一个整数，用于设置可以放入队列中的任务数的上限，当达到这个大小的时候，插入操作将阻塞，直到队列中的任务被消除掉。默认maxsize=0，即任务数量为无限大。

### 添加数据

```python
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
# True
print(f"Is it full ? {q.full()}")
# False
print(f"Is it empty ? {q.empty()}")
# 5
print(f"the size of queue = {q.qsize()}")
```

​	`Queue.put(item, block=True, timeout=None)`将Item放入队列，如果可选参数block是True并且timeout是None，则在必要时阻塞，直到空闲插槽可用，如果timeout是正数，将最多阻塞timeout秒，如果这段时间没有可用的空闲插槽，则引发full异常。反之block为False，如果插槽空闲，则立即使用，把item放入队列，否则引发Full异常。

​	`Queue.full()` 当队列任务已满时，返回的结果为True。如果full()返回True不保证后续调用get()不被阻塞，同样的道理，如果full()返回False也不保证后续调用put()不被阻塞。

​	`Queue.empty()` 如果队列为空，则返回True，否则返回False。如果empty()返回True，不保证后续调用put()会被阻塞。类似的，如果empty()返回False，也不保证后续调用get()会被阻塞。

​	`Queue.qsize()` 返回队列的大小。注意qsize>0不保证后续的get()有可能被阻塞，qsize<maxsize也不保证put()有可能被阻塞。

### 获取

```python
num = q.get()
# num=1
```

`Queue.get(block=True, timeout=None)` 从对列中移除并返回一个数据。当队列为空值，将一直等待。

`Queue.task_done()`：表示前面的排队任务已经完成，被队列的消费者线程使用。每个get()被用于获取一个任务，后续调用task_done()告诉队列，该任务的处理已经完成。如果join()当前正在阻塞，在所有条目都被处理后，将解除阻塞（意味着每个put()进队列的条目task_done()都被收到）。



## 二、生产者-消费者模型

​	生产者模块儿负责产生数据，放入缓冲区，这些数据由另一个消费者模块儿来从缓冲区取出并进行消费者相应的处理。该模式的优点在于：

- 解耦：缓冲区的存在可以让生产者和消费者降低互相之间的依赖性，一个模块儿代码变化，不会直接影响另一个模块儿
- 并发：由于缓冲区，生产者和消费者不是直接调用，而是两个独立的并发主体，生产者产生数据之后把它放入缓冲区，就继续生产数据，不依赖消费者的处理速度

​       在Python中，队列是最常用的线程间的通信方法，因为它是线程安全的，自带锁。而Condition等需要额外加锁的代码操作，在编程对死锁现象要很小心，Queue就不用担心这个问题。

```python
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
```

输出

```shell
======包子铺营业中========
狗不理包子铺现有包子1
Alice吃了包子1


狗不理包子铺现有包子2
Bob吃了包子2


狗不理包子铺现有包子3

Alice吃了包子3

狗不理包子铺现有包子4

Bob吃了包子4

狗不理包子铺现有包子5

Alice吃了包子5

狗不理包子铺现有包子6

Bob吃了包子6
```

