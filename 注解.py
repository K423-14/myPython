# 基础容器类型注解
var_1 : tuple = (1, 2, 3)

# 容器类型详细注解
# 元组必须全都给，字典必须给所有键值对
var_2 : tuple[int, str, bool] = (1, "hello", True)
# 在注释中
var_3 = {"a": 1, "b": 2}  # type : dict[str, int]

# 方法注解
def func(data: str) -> str:
    return data
print(func(1))

# 联合注解
from typing import Union
var_4 : Union[int, str] = [1, 2, 'hello']

