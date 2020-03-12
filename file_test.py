# #  练习1：读取以下文件：a-全部内容；b-每一行的内容；c-读取所有行的内容
# f = open('D:\\code\\vip5\\data.txt', 'r')
# print(f.read())
# f.close()
#
# # b-每一行的内容；c-读取所有行的内容
# f.seek(0)
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
#
#
# #c-读取所有行的内容
# f = open('D:\\code\\vip5\\data.txt', 'r')
# f.seek(0)
# lines = f.readlines()
# for line in lines:
#     print(line,end='')
#
# f.close()

#练习2：读取以下文件的全部内容，并将所有的数字去重后，放入一个列表
# l = []
# with open('D:\\code\\vip5\\data.txt', 'r') as f:
#     lines = f.readlines()
#
# for line in lines:
#     if line not in l:
#         l.append(line)
#
# print(l)

# 练习3：将以上文件的全部内容写入一个新的文件，并按照从小到大的顺序




