# 控制行数
for i in range(1, 10):
    # 控制每行算式的个数
    for j in range(1, i+1):
        # \t 制表符可以规范输出相当于四个空格一下tab
        print(f'{i}*{j}={i*j}', end='\t')
    print()
