
import threading
import time

class myThread (threading.Thread):
   def __init__(self, name):
      threading.Thread.__init__(self)
      self.name = name
      self.c = 0

   def run(self):
      while self.c < 10:
         print ("Starting " + self.name, self.c)
         threadLock.acquire()
         print ("%s: %s" % (self.name, time.ctime(time.time())))
         # if self.name == "Thread-1":
         #    time.sleep(2)
         self.c += 1
         threadLock.release()


threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread("Thread-1")
thread2 = myThread("Thread-2")

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

