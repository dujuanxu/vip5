import os
import shutil

# print(os.path.abspath('D:\\code\\vip5\\data.txt'))
# print(os.path.basename('D:\\code\\vip5\\data.txt'))
# print(os.path.dirname('D:\\code\\vip5\\data.txt'))
# print(os.path.exists('D:\\code\\vip5\\data.txt'))
# print(os.path.join('D:\\code\\vip5\\data.txt','data'))
# print(os.path.realpath('D:\\code\\vip5\\data.txt'))
# print(os.path.split('D:\\code\\vip5\\data.txt'))


# 练习：
# 目录下有这些文件：
# A1.txt
# B2.txt
# C1.doc
# D1.excel
# 任务1-将该目录下的文件按照后缀进行分类，然后分别新建且放入不同的文件夹内，比如txt文件放入txt目录下等


dir = r'/a'

file_l = dict()
if os.path.isdir(dir):
    for f in os.listdir(dir):
        print(f)
        if os.path.isfile(os.path.join(dir, f)):
            file_type = f.split('.')[-1]
            if file_type not in file_l.keys():
                file_l[file_type] = [f]
            else:
                pass
                file_l[file_type].append(f)


for new_dir in file_l.keys():
    os.chdir(dir)
    os.mkdir(new_dir)
    for f in file_l[new_dir]:
        shutil.move(os.path.join(dir, f), os.path.join(dir, new_dir, f) )




