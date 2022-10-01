# def info(a):
#     print(a)
#
#
# info('大爷')


# # 不可变类型的参数
# a = 1
#
#
# def f(a):
#     a = 12
#     print(a)
#
#
# f(a)
# print(a)


# 可变类型的参数
li = [1, 2, 3]


def info(li):
    li.append(12)
    print(li)


info(li)
print(li)
