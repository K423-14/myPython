import json
from data_define import Record


class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.recorders = []

    def read_file(self):
        with open(self.file_path, 'r') as f:
            records = f.readlines()
            for record in records:
                date, order_id, money, province = record.split(',')
                self.recorders.append(Record(date, order_id, money, province))
        f.close()


class JsonReader(FileReader):
    def read_file(self):
        with open(self.file_path, 'r') as f:
            # records = json.load(f)
            records = f.readlines()
            for record in records:
                record = json.loads(record)
                date = record["date"]
                order_id = record["order_id"]
                money = record["money"]
                province = record["province"]
                self.recorders.append(Record(date, order_id, money, province))
        f.close()


if __name__ == "__main__":
    text_file_reader = FileReader('数据分析案例/2011年1月销售数据.txt')
    text_file_reader.read_file()
    print(text_file_reader.recorders[98].money)
    json_file_reader = JsonReader('数据分析案例/2011年2月销售数据JSON.txt')
    json_file_reader.read_file()
    print(json_file_reader.recorders[0].order_id)

