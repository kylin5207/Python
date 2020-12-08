# -- coding = 'utf-8' -- 
# Author Kylin
# Python Version 3.7.3
# OS macOS
"""
多进程间通信：Queue队列
    目的：解耦

"""
import multiprocessing


def download_web(q):
    """
    模拟下载数据的进程
    :return:
    """
    # 1. 模拟下载到的数据
    data = [11, 22, 33, 44]

    # 2. 向队列中写入数据
    for temp in data:
        q.put(temp)

    print("----下载器已经下载完毕----")


def analysis_data(q):
    """
    模拟数据处理进程
    :return:
    """
    waiting_analysis = list()

    # 1. 从队列中获取数据
    while True:
        data = q.get()
        waiting_analysis.append(data)

        if q.empty():
            break

    print("----分析完毕：%s----" % str(waiting_analysis))


def main():
    # 1. 创建一个队列
    queue = multiprocessing.Queue(4)

    # 2. 创建多个进程，将队列的引用当作实参进行传递到里面
    p1 = multiprocessing.Process(target=download_web, args=(queue,))
    p2 = multiprocessing.Process(target=analysis_data, args=(queue,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()


