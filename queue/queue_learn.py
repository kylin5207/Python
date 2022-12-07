import queue

# 创建队列，默认任务数量为无限大
q = queue.Queue(maxsize=5)

q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
print("======q======")
print(q)
print(f"Is it full ? {q.full()}")
print(f"Is it empty ? {q.empty()}")
print(f"the size of queue = {q.qsize()}")

num = q.get()
print(num)
