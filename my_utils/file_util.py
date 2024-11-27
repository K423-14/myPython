def print_file_info(file_name):
    f = None
    try:
        with open(file_name, 'r') as f:
            data = f.readlines()
        for line in data:
            print(line)
    except Exception as e:
        print("Error: " + str(e))
    # 无论怎样都会执行的代码
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    with open(file_name, 'a') as f:
        f.write(data)
    f.close()


if __name__ == "__main__":
    print_file_info("bill.txt")
