# logging

## 一、简介

- logging提供了一组便利的函数，用来做简单的日志。

  日志是用来记录程序在运行过程中发生的状况，在程序开发过程中添加日志模块能够帮助我们了解程序运行过程中发生了哪些事件，这些事件也有轻重之分。

- logging以严重程度递增排序：

    DEBUG:详细信息，一般只在调试问题时使用

    INFO：证明事情按预期工作

    WARNING：某些没有预料到的时间提示，或者在将来可能会出现的问题提示。例如：磁盘空间不足，但是软件还是会照常运作

    ERROR：由于更严重的问题，软件已不能执行一些功能了

    CRITICAL：严重错误，表明软件已不能继续运行了

    级别排序：CRITICAL>ERROR>WARNING>INFO>DEBUG

    默认等级是WARNING。



## 二、使用

```python
import logging
logging.debug('debug 信息')
logging.warning('只有这个会输出。。。')
logging.info('info 信息')
```

> 默认等级为warning，因此等级低于warning的信息，无法展示在控制台。

- 设置日志显示级别\保存到指定文件

通过 logging.basicConfig() 可以设置 root 的日志级别和日志输出格式。

```python
logging.basicConfig(filename="xxx.log", level=logging.DEBUG)
```

> - Logging.basicConfig() 需要在开头就设置，在中间设置并无作用
> - filename：指定日志保存路径
> - level：日志等级（默认warning）



## 三、print与logging

- print

  - **print()**函数接受一个字符串消息或者一个可以转换为字符串的对象, 用于在标准输出上打印字符串。但是，它并不是线程安全的。默认情况下，消息不会刷新到标准输出，直到内部缓冲区已满。可以在每次调用后强制刷新消息，这可以通过将“ **flush** ”参数设置为**True**来实现。

  - 从多个线程调用打印不是线程安全的，并且可能会导致消息损坏，因为线程是上下文切换的。

    ```python
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
    ```

  >```python
  >Thread 24 got 0.0003701930798365449.
  >Thread 71 got 0.006846710140869572.
  >Thread 62 got 0.009786948310893995.
  >Thread 29 got 0.015333791349448567.
  >Thread 34 got 0.014324192982556494.
  >Thread 96 got 0.04343789143526011.
  >Thread 75 got 0.04845865198851296.
  >Thread 79 got 0.05445974657902397.Thread 68 got 0.057677852311460276.
  >
  >Thread 48 got 0.06794532818839316.
  >```

- print默认的输出流为sys.stdout, logging为sys.stderr。

  可以手动转换：

  ```
  import sys
  
  logger = logging.getLogger('simple_logger')
  logger.setLevel(logging.INFO)
  handler = logging.StreamHandler(sys.stdout)
  logger.addHandler(handler)
  ```

  >​	**<font color='red'>虽然使用如下的方式手动将logging的输出流改为sys.stdout，由于其内部实现是线程安全的（more thread-safe），最终输出不会乱序</font>**

- print是线程不安全的，logging内置了锁的操作是线程安全的。可参考文档：

print：https://superfastpython.com/thread-safe-print-in-python/
logging: https://superfastpython.com/thread-safe-logging-in-python/

- 在logging模块的内部，使用互斥（mutex）锁来确保日志记录处理程序免受来自多个线程的竞争条件的影响。例如，锁用于确保一次只有一个线程写入日志文件或日志流。这确保了日志消息被序列化并且没有被破坏。

*It achieves this though using threading locks; there is one lock to serialize access to the module’s shared data, and each handler also creates a lock to serialize access to its underlying I/O.*

```python
from random import random
from time import sleep
from threading import Thread
import logging

# task to be executed by worker threads
def task(number, threshold):
    # simulate doing work
    for i in range(5):
        # generate value
        value = random()
        # block
        sleep(value)
        # check if is a problem
        if value < threshold:
            logging.warning(f'Thread {number} value less than {threshold}, stopping.')
            break
    logging.info(f'Thread {number} completed successfully.')


# configure the log to report all messages
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# start the threads
threads = [Thread(target=task, args=(i, 0.1)) for i in range(5)]

# start threads
for thread in threads:
    thread.start()
# wait for threads to finish
for thread in threads:
    thread.join()

```

>```shell
>WARNING:root:Thread 1 value less than 0.1, stopping.
>INFO:root:Thread 1 completed successfully.
>WARNING:root:Thread 2 value less than 0.1, stopping.
>INFO:root:Thread 2 completed successfully.
>INFO:root:Thread 4 completed successfully.
>INFO:root:Thread 3 completed successfully.
>INFO:root:Thread 0 completed successfully.
>```

​	如果日志记录不是线程安全的，那么日志消息将不会被正确序列化，当多个线程试图同时写入标准输出流时，可能会重叠和损坏。

- 如何使print更安全？

  为了使**print()**函数线程安全，需要将其视为临界区并使用互斥（mutex）锁进行保护，例如通过**threading.Lock**类的实例来实现。

- python中的一些常用的数据结构，比如队列`queue.Queue`。就是一个线程安全的数据结构，作为对象的消息可以通过`put()`添加到该结构上，并通过`get()`删除和检索。