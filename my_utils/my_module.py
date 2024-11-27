'''
def test(x, y):
    return x + y

# 直接运行my_module.py时，__name__的值为__main__，而当my_module.py被其他模块引入时，__name__的值为my_module
print(__name__)
'''

def test_a(x, y):
    return x + y

def test_b(x, y):
    return x - y

__all__ = ['test_a']  # 只导入test_a函数，只在 * 上作用，手动导入不受影响，在__init__.py中设置