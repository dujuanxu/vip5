# 读取data文件中的数据，将所有的数字去重并按照从小到大的顺序写入backup文件
#11
#2
#22
#13
#2
#13
l = []
with open('D:\\code\\vip5\\data3.txt', 'r', encoding="utf-8") as f:
    for line in f:
        # print(line,end='')