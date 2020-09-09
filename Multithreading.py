'''
A process can be divide into smaller units called Threads,which is an independent part of execution.


Multitasking : At one point we can run multiple apps(E.g MS Word, VLC ,etc at the same time).They do not actually run
simultaneously, but CPU schedule the time in such a way that it seems that they are running together.However if multiple
cores are present in CPU, it is possible to run different apps simultaneously.

Multithreading : Its like doing multitasking,but within a same app. E.g. , while doing MS Word , at the same time we are typing ,
spell check ,autosave etc is are happening .Different threads are responsible to perform this .It is called multithreading.

'''


class Hello:

    def run(self):
        for i in range(5):
            print("Hello")


class Hi:

    def run(self):
        for i in range(5):
            print("Hi")


t1 = Hello()
t2 = Hi()

t1.run()     #Every program has by default one thread even if we do not create it,which is main thread.
t2.run()


'''
Suppose we want to run both the functions simultaneously, then we need to do multithreading
'''
from threading import *
from time import sleep
class Hello(Thread):

    def run(self):
        for i in range(5):
            print("Hello")
            sleep(5)


class Hi(Thread):

    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()

t2.start()  #after calling start() , we have three threads , main ,t1,t2
t1.run()
sleep(0.2)   #to avoid collision
t2.run()
sleep(0.2)


print("Bye")     #It will print in between,not in the last, since it is executed by main thread , and main thread gets actvated
             # as soon as t1 and t2 starts.
''' To avoid this , use join() in t1 and t2.'''


t1.join()
t2.join()

print("Bye bye")