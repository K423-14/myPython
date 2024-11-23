ages = [21, 25, 21, 23, 22, 20]
ages.append(31)
# 追加列表
ages.extend([29, 33, 30])
# ages += [29, 33, 30]
print(ages[0])
print(ages[ages.__len__() - 1])
print(ages[len(ages) - 1])
print(ages[-1])
# 查找
print(ages.index(31))
# 切片
# [起始:结束:步长]，可以省略任意一个参数
print(ages[::2])  # 从头到尾，步长为2
print(ages[:])  # 从头到尾，步长为1
print(ages[3:1:-1])  # 从下标为3的元素到下标为1的元素，步长为-1

# 初始化元组
t1 = ("hello", )  # 如果元组中只有一个元素，需要在元素后面加逗号

# 字符串
mystr = "itheima itcast boxuegu"
# 统计
print(mystr.count("it"))
mystr = mystr.replace(" ", "|")
mystr = mystr.split("|")
print(mystr[1][::-1])
# mystr1 = mystr.split("|")[0]
# print(mystr1[6::-1])

# 集合：不支持索引！！！
my_list = ['黑马程序员', '传智播客', '博学谷', '黑马程序员', 'itcast', 'itheima', '黑马程序员', 'best']
# mySet = {}  # 这样定义的是字典
my_set = set()
for i in my_list:
    # 集合添加元素
    my_set.add(i)
print(my_set)
# 移除元素
my_set.remove('best')
# 随即取出一个元素
print(my_set.pop())
# 青空集合
my_set.clear()
# 集合操作
my_set = {1, 2, 3, 4, 5}
my_set1 = {4, 5, 6, 7, 8}
# print(my_set.difference(my_set1))  # 一有二没有
my_set.difference_update(my_set1)  # 消除差集
print(my_set)
# print(my_set.union(my_set1))  # 并集，不确定顺序


# 字典
staffs = {"王力宏": ["科技部", 3000, 1], 
          "周杰伦": ["市场部", 5000, 2],
          "林俊杰": ["人事部", 7000, 1]
        }
# 添加元素
staffs["张学友"] = ["财务部", 9000, 2]
# 删除元素，清空clear()
staffs.pop("王力宏")
for key in staffs:
    if staffs[key][2] == 1:
        staffs[key][1] += 1000
    print("{0}: 部门: {1}, 工资: {2}, 级别: {3}".format(key, staffs[key][0], staffs[key][1], staffs[key][2]))

# 排序，以上均通用，均变成列表，丢失键值对
sorted(staffs)
