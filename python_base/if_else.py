# # 例子：
# # 1-	if练习--从键盘输入一个数，判断该数是否在列表中，如果在就打印happy
# l = [1,2,3,4,5]
# num = int(input("请输入一个数:"))
#
# if num in l:
#     print('{}在列表中'.format(num))
#
# # 2-	if-else练习—从键盘输入一个数，判断该数是否在列表中，如果在就打印happy，并且让列表中的该值+1，否则打印sad
# num = int(input("请输入一个数:"))
#
# if num in l:
#     print("happy")
#     idx = l.index(num)
#     l[idx] += 1
#     print(l)
# else:
#     print("sad")

# 3-	输入一个数，判断该数的范围：90-100：等价为A……60以下：等级为E注：
num = int(input("请输入一个数:"))

if 90 <= num <= 100:
    print("A")
elif num > 100 or num < 0:
    print("输入分数错误")
elif 80<= num < 90:
    print("B")
elif 70<=num<60:
    print("C")
else:
    print("E")
# Python不支持&&、||，需要and、or代替，3时也支持多个条件连接：0<a<10
