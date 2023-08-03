import multiprocessing
import time

def do(n):             # 参数n由args=(1,)传入
    print(f"worker {n} start")
    name = multiprocessing.current_process().name        # 获取当前进程的名字
    print(f"{name} is starting")

    time.sleep(20)

    print(f"worker {n} over")
    return


if __name__ == '__main__':
    process_list = []
    for i in range(5):
        p = multiprocessing.Process(target=do, args=(i,))      # (i,)中加入","表示元祖
        process_list.append(p)

    for i in range(5):
        process_list[i].start()  # 用start()方法启动进程，执行do()方法

    for i in range(5):
        process_list[i].join() # 等待子进程结束以后再继续往下运行，通常用于进程间的同步