'''
进程(一个程序) > 线程

设计模式：
    单例模式：创建一个tools对象，其他人之调用它而不实例化另一个tool
    工厂模式：创建一个工厂实例化多继承对象

'''
import time
import threading

def sing(msg):
    while(True):
        print(msg)
        time.sleep(1)

def dance(msg):
    while(True):
        print(msg)
        time.sleep(1)


sing_thread = threading.Thread(target=sing, args=("开始唱歌，啊啊啊~", ))  # 元组传参数要有,
dance_thrade = threading.Thread(target=dance, kwargs={'msg': '开始跳舞，啦啦啦~'})

sing_thread.start()
dance_thrade.start()
