import csv
filename = 'fyx_chinamoney.csv'  # csv 文件名
batch_size = 80  # 每个批次的大小为 80

with open(filename, 'r') as file:
    lst = file.readlines()  # 读取 csv 文件中的所有数据

lst = [line.strip() for line in lst]  # 去除每行数据的换行符

for i in range(0, len(lst), batch_size):
    batch = lst[i:i+batch_size]  # 使用切片获取当前批次的数组
    print(batch)  # 打印当前批次的数组
