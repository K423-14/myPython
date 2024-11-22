import random

sum = 10000

for i in range(20):
    performance = random.randint(1, 10)
    if performance >= 5:
        sum -= 1000
        print("向员工{0}发放工资1000元，账户余额还剩余{1}元。".format(i, sum))
    else:
        print("员工{0}，绩效分为{1}，低于5,不发工资，下一位。".format(i, performance))
    if(sum == 0):
        print("工资发完了，下个月领取吧")
        break

