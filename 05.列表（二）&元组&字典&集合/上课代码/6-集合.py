# s = {}  # 创建的是空字典
# s = set()  # 创建的是空集合
# print(type(s))


# s = {1, '2', 3, 3}
# print(s)


# s = set('aabbcc')
# print(s)


# 集合.add(元素)  只能添加不可变类型的元素
# s = set('abc')
# print(s)
# s.add('abc')
# s.add(1)
# s.add(1.0)
# dic = dict(n=1)
# s.add(dic)
# print(s)
# update只能添加可迭代对象或者序列
# 可迭代对象或者序列：里面的元素可以一个一个取出来的
# s.update([1, 2])
# s.update('jkl')
# s.update(123)
# print(s)


s = set('abc')
print(s)
# s.remove('a')
# print(s)
s.clear()
print(s)
