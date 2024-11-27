with open('bill.txt', 'r') as f_r:
    data = f_r.readlines()
    with open('bill.txt.bak', 'w') as f_w:
        for i in data:
            if '测试' not in i:
                f_w.write(i)
f_w.close()
f_r.close()
