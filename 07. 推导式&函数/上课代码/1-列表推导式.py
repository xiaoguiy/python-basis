# eg1：生成一个[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5,
# 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]的列表


# 起始值、结束值、步长是不能为浮点数的
# 左闭右开
# for i in range(1, 21, 1):
#     print(i/2)
# li = [1, 2, 3]
# for i in li:
#     print(i)
# 创建一个空列表存储
# li = []
# for i in range(1, 21, 1):
#     li.append(i/2)
# print(li)


# 列表推导式一：
# 语法：[需要加到列表里面的值 for 变量 in 序列]
# li = [i/2 for i in range(1, 21, 1)]
# print(li)


# eg1：有列表 li 如下，筛选出 li 中小于0的数进行平方，添加至新列表中
#
li = [6, 2, 6, 7, -15, 8, -17, -10, -15, -4]
# 创建一个空列表来存储目标值
# li_result = []
# li = [6, 2, 6, 7, -15, 8, -17, -10, -15, -4]
# for i in li:
#     if i < 0:
#         li_result.append(i**2)
# print(li_result)


# 列表推导式二
# 语法：[需要放到列表里面的元素 for 变量 in 序列 if 条件]
# li = [j**2 for j in li if j < 0]
# print(li)


# 现有字符串'abc'和'123',根据这个两个字符串打印输出
# ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
a = 'abc'
b = '123'
# li = []
# for i in b:
#     for j in a:
#         li.append(i+j)
# print(li)


# 列表推导式三
# 语法：[需要加到列表里面的东西 for 变量1 in 序列1 for 变量2 in 变量2]
# li = [i+j for i in b for j in a]
# print(li)
