#coding:cp936 ---*
'''这段程序的存在是为了测试pycharm的调试性能'''
import threading
import time
def get_thread_name():
    t=threading.current_thread()
    return t.name
def print_time(delay):
    '''define a funtion for the thread.'''
    thread_name=get_thread_name()
    count=0
    while count< 8:
        time.sleep(delay)
        count+=1
        print("%s: %s" %(thread_name,time.ctime(time.time())))

#create two thread as follows
t1=threading.Thread(target=print_time,args=(1,))
t2=threading.Thread(target=print_time(),args=(2,))
t1.start()
t2.start()
t1.join()
t2.join()


