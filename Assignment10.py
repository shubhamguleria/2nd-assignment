#Question1
'''
import time
import threading
from threading import Thread
def sleep():
    print("\nThread %d: Is going to sleep for 5 sec."%i)
    time.sleep(5)
    print("\nThread %d: woke up."%i)
        
for i in range(3):
    th=Thread(target=sleep)
    th.start()
'''
#Question2
'''
import time
import threading
from threading import Thread
def num():
    for i in range(1,11):
        print("%i"%i)
        time.sleep(1)
def fun():
    th=Thread(target=num)
    th.start()
'''
#Question3
'''
import time
import threading
from threading import Thread
def num():
    for t in [2,4,6,8,10]:
        print("Element display for %s sec."%t)
        time.sleep(t)
def fun():
    th=Thread(target=num)
    th.start()
'''
#Question4
'''
import threading
import math
class f(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        global result
        temp = math.factorial(self.num)
        print("\n%s: calculate %d's factorial is %d" %(self.name,self.num,temp))
        result += temp
result = 0
threads = []
def test():
    for i in range(1,6):
        t = f(i)
        threads.append(t)
    for i in range(5):
        threads[i].start()
    for i in range(5):
        threads[i].join()
'''
