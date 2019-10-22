import test_
import time

tm = time.time()
for i in range(10):
    # test_.count(1,1)
    test_.io()
print("Single cpu:",time.time() - tm)