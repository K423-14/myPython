def atm(account_amount):
    def action(num, deposit=True):

        # 要想修改外层参数，需要下面这句话
        nonlocal account_amount

        if deposit:
            account_amount += num
            print(f"存款：+{num}，账户余额：{account_amount}")
        else:
            account_amount -= num
            print(f"取款：-{num}，账户余额：{account_amount}")

    # 要返回
    return action

# 防止总金额被随意篡改
my_atm = atm(0)
my_atm(300)
my_atm(300)
my_atm(100, False)
