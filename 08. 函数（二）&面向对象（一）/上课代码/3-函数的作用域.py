# 局部作用域

# def f():
#     a = '辣条'
#     print(a)
#
#
# f()
# print(a)


# def info(a):
#     print(f'儿子拿到了{a}')
#
#
# def f():
#     food = '华子'
#     info(food)
#
#
# f()
# print(food)


# 全局变量
# food = '华子'
#
#
# def f():
#     print(food)
#
#
# f()
# print(food)
#
#
# n = float(1)
# print(n)


a = 1


def f():
    global a
    a = 10
    print(a)


f()
print(a)
