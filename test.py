import signal
import time

def handler(num, frame):
    with open("/home/mathkuro/work/python/hoge.txt", "w+") as f:
        f.write(str(num))
        f.write(str(frame))

signal.signal(signal.SIGHUP, handler)

for i in range(100):
    time.sleep(1)
