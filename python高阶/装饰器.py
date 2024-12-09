from random import randint
from time import sleep

# # 装饰器的一般写法，闭包
# def outer(func):
#     def inner():
#         print("开始执行")
#         func()
#         print("结束执行")
#     return inner

# def my_sleep():
#     print("睡眠中......")
#     sleep(randint(1, 10))


# fn1 = outer(my_sleep)
# fn1()


# 装饰器
def outer(func):
    def inner():
        print("开始执行")
        func()
        print("结束执行")
    return inner

@outer
def my_sleep():
    print("睡眠中......")
    sleep(randint(1, 10))


my_sleep()
