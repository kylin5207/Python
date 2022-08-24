import threading
import subprocess
from queue import Queue

send_info = Queue()

def async_call(func):
    def wrapper(*args, **kwargs):
        thr = threading.Thread(target=func, args=args, kwargs=kwargs)
        thr.start()

    return wrapper

@async_call
def get_result():
    cmd = "python3 go.py"
    res = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE
                           )
    for info in iter(res.stdout.readline, b''):
        send_info.put(info)

def main():
    global send_info
    get_result()
    while True:
        try:
            data = send_info.get(timeout=2)
            data = data.decode('utf-8')
            print(data)
        except Exception as e:
            break

if __name__ == "__main__":
    main()