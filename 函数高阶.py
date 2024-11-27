'''
# gender='男' 是默认参数
def user_info(name, age, gender='男'):
    print(f'您的姓名是{name}, 年龄是{age}, 性别是{gender}')

# 位置参数
user_info('小明', 18, '男')
# 关键字参数
user_info(age=20, name='小红', gender='女')
# 混合使用
user_info('小李', age=11, gender='男')
          
'''

# 位置传递，arg是元组，数量不限arguments
def user_info(*args):
    print(args)

user_info('TOm', 18)

# 关键字传递，kwargs是字典，数量不县key-word
def user_info(**kwargs):
    print(kwargs)

user_info(name='tom', age=18)

# 函数调用
def test_func(compute):
    print(compute(1, 2))

def compute(x, y):
    return x + y

test_func(compute=compute)
# 匿名函数，运行代码只有一行
test_func(lambda x, y : x + y)
