"""
多进程的简单实用
"""
import multiprocessing


def do(n):             # 参数n由args=(1,)传入
    name = multiprocessing.current_process().name        # 获取当前进程的名字
    print(f"{name} is starting")
    print(f"worker {n}")
    return


if __name__ == '__main__':
    numList = []
    for i in range(5):
        p = multiprocessing.Process(target=do, args=(i,))      # (i,)中加入","表示元祖
        numList.append(p)
        print(numList)
        p.start()                 # 用start()方法启动进程，执行do()方法
        p.join()                  # 等待子进程结束以后再继续往下运行，通常用于进程间的同步
        print("Process end.")