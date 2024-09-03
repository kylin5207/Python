import threading
import logging

# 设置日志级别为 DEBUG
# 配置日志格式
logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
logger = logging.getLogger(__name__)


# Using print
def function_with_print(x, y):
    print(f"some_function called with args: {x}, {y}")
    result = x + y
    print(f"Result: {result}")
    return result


# Using logging
def function_with_logging(x, y):
    logger.debug(f"some_function called with args: {x}, {y}")
    result = x + y
    logger.info(f"Result: {result}")
    return result


if __name__ == "__main__":
    # def thread_task():
    #     for i in range(3):
    #         function_with_print(i, i * 2)
    #
    #
    # # 创建多个线程
    # threads = []
    # for i in range(3):
    #     thread = threading.Thread(target=thread_task, name=f"Thread-Print-{i + 1}")
    #     threads.append(thread)
    #     thread.start()
    #
    # # 等待所有线程完成
    # for thread in threads:
    #     thread.join()


    def thread_task():
        for i in range(3):
            function_with_logging(i, i * 2)


    # 创建多个线程
    threads = []
    for i in range(3):
        thread = threading.Thread(target=thread_task, name=f"Thread-{i + 1}")
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

