# 1.求n以内的质数（只能被1和它本身整除）
def get_grime_num(n):
    l = []
    if n < 2:
        print("没有质数")
        return l
    if n == 2:
        l.append(2)
        return [2]

    i = 2
    while i <= n:
        j = 2
        while j < i:
            if i % j == 0:
                break
            j += 1

        if j == i:
            l.append(i)
        i += 1
    return l


# 2.求10个斐波那契数列 1 1 2 3 5 8 13 ……
def fibonacci(n):
    if n < 0:
        return("个数必须>0")
    if n <= 2:
        return [1]*n

    f = [1, 1]
    i = 0
    while i<=n:
        f.append(f[-1]+f[-2])
        i += 1
    return  f

# 3. 读取data文件中的数据，将所有的数字去重并按照从小到大的顺序写入backup文件
#11
#2
#22
#13
#2
#13

def copy_file_asc(src_file, des_file):
    l = []
    with open(src_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            s = int(line.strip())
            if s not in l:
                l.append(s)
    l.sort()

    with open(des_file, 'w+') as f:
        for i in l:
            print(i)
            f.write(str(i)+'\n')

    return True

# 4. 读取以下文件的全部内容，并将所有的数字去重后，放入一个列表
# 文件内容如下：
#11，10，8
#2，23，24
#22，1，0
#13，7
#5
#29，19
#10，1，3，5，9
def sort_num_form_file(src_file):
    l = []
    with open(src_file, 'r', encoding='utf-8') as f:
        for line in f:
            row = line.strip().split(',')
            for s in row:
                num = int(s.strip())
                if num not in l:
                    l.append(num)

    l.sort()
    return l


if __name__ == '__main__':
    l = sort_num_form_file("/data3.txt")
    print(l)
    copy_file_asc("/data.txt", "/python_base/backup.txt")
    print(get_grime_num(20))
    print(fibonacci(10))
