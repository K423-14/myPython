# from data_define import Record
from file_define import FileReader, JsonReader
from data_define import Record

my_reader1 = FileReader("数据分析案例/2011年1月销售数据.txt")
my_reader2 = JsonReader("数据分析案例/2011年2月销售数据JSON.txt")

my_reader1.read_file()
my_reader2.read_file()

all_data : list[Record] = my_reader2.recorders + my_reader1.recorders

date_dict : dict[str, int] = {}
for data in all_data:
    if data.date in date_dict.keys():
        date_dict[data.date] += data.money
    else:
        date_dict[data.date] = data.money

print(date_dict)
