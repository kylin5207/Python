# -*- coding:utf-8 -*-
"""
test1
通过多线程实现类似于linux中的>>功能，将日志记录到指定的文件中
:Author: Shangmengqi@tsingj.com
:Last Modified by: Shangmengqi@tsingj.com
"""
import os, sys
import codecs
from threading import Thread, Lock

class TraceLog(Thread):
    def __init__(self, logName):
        super(TraceLog, self).__init__()
        self.logName = logName
        self.lock = Lock()
        self.contexts = []
        self.isFile()

    def isFile(self):
        if not os.path.exists(self.logName):
            with codecs.open(self.logName, 'w') as f:
                f.write(f"This log name is {self.logName}\n")
                f.write("Start log\n")

    def write(self, context):
        # 将需要输出的内容追加至列表中
        self.contexts.append(context)

    def run(self):
        while True:
            self.lock.acquire()
            if len(self.contexts) != 0:
                with codecs.open(self.logName, 'a') as f:
                    # 追加方式写入文件
                    for context in self.contexts:
                        f.write(context)
                # 每次写完后清空列表
                del self.contexts[:]
            self.lock.release()


class Server(object):
    def log(self):
        print("Start server")

        for i in range(100):
            print(i)

        print("End server")

if __name__ == "__main__":
    traceLog = TraceLog("main.log")
    traceLog.start()
    sys.stdout = traceLog
    sys.stderr = traceLog
    server = Server()
    server.log()