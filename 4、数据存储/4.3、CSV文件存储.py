# 1、写入

import csv
import pandas
# with open('data.csv', 'w', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', '张三', '10'])
#     writer.writerow(['10002', '李四', '11'])
#     writer.writerow(['10002', '王二', '12'])

# 2、读取

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)