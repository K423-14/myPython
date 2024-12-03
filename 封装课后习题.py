class mobile:
    # python私有使用__开头
    __is_5g_enable = True

    def __init__(self, price):
        self.price = price

    # 魔术方法，__**__定义的
    # 小于，le小于等于，gt大于，ge大于等于，eq等于，ne不等于
    def __lt__(self, other):
        return self.price < other.price
    
    # 重写打印方法
    def __str__(self):
        return "mobile price is %s" % self.price
    
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")
        
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")
    
    
mobile1 = mobile(1000)
mobile2 = mobile(2000)
print(mobile1 > mobile2)


