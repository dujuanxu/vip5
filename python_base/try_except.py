#捕捉除零错----1.已知异常类型
# def calc(c, d):
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("除数不能为0")
#
#
# a, b = input().split()
# calc(int(a), int(b))

#--2.未知异常
# def calc(c, d):
#     try:
#         print(c/d)
#     except BaseException:
#         print("除数不能为0")
#
#
# a, b = input().split()
# calc(int(a), int(b))

#----3.多重异常
def calc(c, d):
    try:
        print(c/d)
        print(e)
    except NameError:
        print("该对象未声明")
    except BaseException:
        print("除数不能为0")

a = input('-')
b = input('-')
calc(int(a), int(b))

#---4.不管有没有抛出异常，都执行finally
# def calc(c, d):
#     try:
#         print(c/d)
#     except NameError:
#         print("该对象未声明")
#     except BaseException:
#         print("除数不能为0")
#     finally:
#         print("程序执行完毕。。")
#
# a = input('-')
# b = input('-')
# calc(int(a), int(b))

# --5.没有抛出异常时，继续执行elese语句
# def calc(c, d):
#     try:
#         print(c/d)
#     except NameError:
#         print("该对象未声明")
#     except BaseException:
#         print("除数不能为0")
#     else:
#         print("程序执行完毕。。")
#
# a = input('-')
# b = input('-')
# calc(int(a), int(b))
