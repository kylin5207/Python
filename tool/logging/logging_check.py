from random import random
from time import sleep
from threading import Thread
import logging
import sys
"""
logging自带锁，保证线程安全
"""

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
# handler = logging.StreamHandler(sys.stdout)
# logger.addHandler(handler)
# configure the log to report all messages to file
# logging.basicConfig(filename='application.log', level=logging.DEBUG)

# start the threads
threads = [Thread(target=task, args=(i, 0.1)) for i in range(5)]

# start threads
for thread in threads:
    thread.start()
# wait for threads to finish
for thread in threads:
    thread.join()
