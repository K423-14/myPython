from pymysql import connect
from file_define import FileReader, JsonReader


# 文件读取
text_file_reader = FileReader('数据分析案例/2011年1月销售数据.txt')
text_file_reader.read_file()
json_file_reader = JsonReader('数据分析案例/2011年2月销售数据JSON.txt')
json_file_reader.read_file()


# 连接
conn = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='zhe4chang10',
    autocommit=True  # 事务自动批准
)

# 游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('py_sql')
# 插入数据
for r in text_file_reader.recorders:
    # 执行语句
    # cursor.execute("INSERT INTO orders(date, order_id, money, province) VALUES({0}, {1}, {2}, {3})".format(r.date, r.order_id, r.money, r.province))
    cursor.execute("INSERT INTO orders(date, order_id, money, province) VALUES(%s, %s, %s, %s)", (r.date, r.order_id, r.money, r.province))

for r in json_file_reader.recorders:
    # 执行语句
    # cursor.execute("INSERT INTO orders VALUES({0}, {1}, {2}, {3})".format(r.date, r.order_id, r.money, r.province))
    cursor.execute("INSERT INTO orders(date, order_id, money, province) VALUES(%s, %s, %s, %s)", (r.date, r.order_id, r.money, r.province))



cursor.execute("SELECT * FROM orders")
# 接受返回值，元组
result : tuple = cursor.fetchall()
print(result)
# 养成良好习惯
conn.close()




