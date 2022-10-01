# 打印输出 5 次 “hello world”


# i = 2
# while i < 5:
#     print('hello world')
#     i += 1


# 求1-100之间的和
# 1-100  100次
# 获得1-100的数字




"""
1   0+1
1+2  sum_num+2
1+2+3 sum_num+3
1+2+3+...+n  sum_num +i
"""
# 用来存储1-100的和  1+2+3+...+100
# i = 1
# sum_num = 0
# while i < 101:
#     sum_num += i
#     i += 1  # i = i + 1
# print(sum_num)


# 输出1-10之间的数字，当数字为8的时候结束循环
# i = 1
# while i < 11:
#     print(i)
#     if i == 8:
#         break
#     i += 1


# 不让输出8
# 执行continue的时候注意在continue之前将条件改变
# i = 1
# while i < 11:
#     if i == 8:
#         i += 1
#         continue
#     print(i)
#     i += 1


i = 1
while i < 11:
    print(i)
    if i == 8:
        i += 1
        continue
    i += 1
else:
    print('正常结束')
