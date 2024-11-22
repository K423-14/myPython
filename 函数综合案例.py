def save(name, money):
    print("---------------存款----------------")
    deposit = input("请输入您要存款的余额：")
    # 判断输入的是否是数字
    if(deposit.isdigit()):
        money += int(deposit)
        print("{0}您好，您存款{1}元成功".format(name, deposit))
        print("{0}您好，您的余额剩余：{1}".format(name, money))
    return money

def withdraw(name, money):
    print("---------------取款----------------")
    temp = input("请输入您要取的余额：")
    # 判断输入的是否是数字
    if(temp.isdigit()):
        money -= int(temp)
        print("{0}您好，您取款{1}元成功".format(name, temp))
        print("{0}您好，您的余额剩余：{1}".format(name, money))
    return money


def menu(name):
    print("--------------主菜单---------------")
    print("{}您好，欢迎来到黑马银行ATM，请选择操作：".format(name))
    print("查询余额  【输入1】")
    print("存款     【输入2】")
    print("取款     【输入3】")
    print("退出     【输入4】")


if __name__ == "__main__":
    name = input("请输入您的姓名：")
    money = 5000000
    while True:
        menu(name)
        choice = input("请选择您要进行的操作")
        if choice == '1':
            print("---------------查询余额---------------")
            print("{0}您好，您的余额剩余：{1}".format(name, money))
        elif choice == '2':
            money = save(name, money)
        elif choice == '3':
            money = withdraw(name, money)
        else:
            print("退出成功")
            break


