import test_
from threading import Thread
import time
jobs=[]
tm=time.time()
for i in range(10):
    t=Thread(target=test_.count,args=(1,1))
    jobs.append(t)
    t.start()
for i in jobs:
    i.join()
print("Thread cpu:",time.time()-tm)