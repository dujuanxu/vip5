# 设计一个计算器，输入两个数，自动实现加减乘除
def  calculator(a,b):
    print('a+b={}'.format(a+b))
    print('a-b={}'.format(a-b))
    print('a*b={}'.format(a*b))
    print('a/b={}'.format(a/b))

a,b = input().split()
calculator(int(a),int(b))

# （进阶：根据用户输入的计算符号计算结果）
def  calculator(a,o,b):
    if o == '+':
        print('a+b={}'.format(a+b))
    elif o == '-':
        print('a-b={}'.format(a-b))
    elif o == '*':
        print('a*b={}'.format(a*b))
    elif o == '/':
        print('a/b={}'.format(a/b))
    else:
        print("不支持该运算")

a,o,b = input().split()
calculator(int(a), o, int(b))