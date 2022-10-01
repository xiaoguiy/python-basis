# 1.求1+2!+3!+..10!的阶乘，利用循环完成

# n!=1*2*3*...*n
# 存储和
sum_num = 0
for i in range(1, 11):
    # 用于传出积的变量
    ji = 1
    for j in range(1, i+1):
        ji *= j
    sum_num += ji
print(sum_num)



