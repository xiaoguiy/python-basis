# n = 'hello world'
# 找出h
# find 和 index
# 语法：字符串.find(需要找的值)
# print(n.find('h'))  # 0
# 找出l最小下标
# print(n.find('l'))  # 2
# 语法：字符串.index(需要找的值)
# print(n.index('l'))
# print(n.find('k'))  # -1
# print(n.index('k'))


# 替换函数replace
# 语法：字符串.replace(旧值, 新值, 替换的次数)
# n = 'hello world'
# 将字符里面的l替换为p
# print(n.replace('l', 'p'))
# print(n.replace('l', 'p', 2))


# split()
# 语法：字符串.split(分割字符)
# n = 'hello world'
# 不写参数默认根据空格分割，如果有参数就会根据参数分割，字符里面包含几个就分割几次
# print(n.split('l'))


# n = 'hello world'
# print(n.startswith('fj'))
# print(n.endswith('dhgfjsdgjs'))


# n = 'hello world'
# 转大写
# 语法：字符串.upper()
# print(n.upper())
# m = 'HELLO'
# print(m.lower())


# strip()
# 语法：字符串.strip(字符)
# 不给参数默认去掉两端空格，给了参数去掉两端相应字符，注意：只去掉两端的东西
# n = '-hello-world-'
# print(n.strip('-'))


# n = 'hh_hh'
# print(n.isalpha())


# n = '123 123'
# print(n.isdigit())


# join
# 语法：'连接字符'.join(可迭代对象)
# 可迭代对象：里面的元素可以被一个一个取出来的数据类型
n = 'hello'
print('-'.join(n))
