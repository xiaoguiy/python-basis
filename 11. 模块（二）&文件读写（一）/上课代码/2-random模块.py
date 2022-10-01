import random


# print(random.random())
# 利用这个方法产生1-10左闭右开的一个数字
# print(random.random()*10)


# 随机产生整数，两边的边界值都可以取到
# print(random.randint(1, 10))


# 序列：列表、元组、字符串
# 随机从序列里面取出元素，注意：得是序列
# li = [1, 2, 3]
# s = {1, 2, 3}
# print(random.choice(s))  # TypeError: 'set' object does not support indexing


# li = [1, 2, 3, 4]
# li = (1, 2, 3, 4)
# 打乱顺序并返回，注意：只能作用于列表
# print(random.shuffle(li))
# print(li)


# li = [1, 2, 3, 4]
# tup = (1, 2, 3, 4)
# 随机取样，同时得给出取样对象和取样个数
# print(random.sample(tup, 2))


print(random.randrange(1, 11))
