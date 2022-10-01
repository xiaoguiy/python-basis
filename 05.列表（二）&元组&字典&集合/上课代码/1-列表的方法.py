# 删除方法
# li = ['韩信', '澜', '百里', '马超']
# 列表.remove(需要删除的元素)
# 删除列表里面的韩信
# li.remove('韩信')


# 列表.pop(索引)
# 没有给参数默认删除最后一个，给了参数删除下标对应的元素
# 删除澜
# li.pop(1)
#
# print(li)


# li = ['韩信', '澜', '百里', '马超']
# del 和clear
# 语法：del 列表[索引]  删除对应索引的列表元素
# 删除百里
# 语法：del 列表  删除整个列表
# del li[2]
# del li
# print(li)


# 列表.clear() # 仅仅是删除列表里面的内容
# li.clear()
# print(li)


# 新增方法
# 语法：列表.append(需要添加的元素)
# li = ['韩信', '澜', '百里', '马超']
# li.append('玄策')
# li.append(['1', '2'])
# print(li)


# li.extent(序列/可迭代对象)
# 添加的必须是序列或者是可迭代对象
# li.extend(['1', '2'])
# li.extend(123)
# print(li)


# 列表.insert(索引, 元素) 添加元素到指定索引的前面
# li = ['韩信', '澜', '百里', '马超']
# 在澜的前面加个蔡文姬
# li.insert(1, '蔡文姬')
# li.insert(2, '蔡文姬')
# print(li)


# 其他
# 列表.count(查看的元素)  查看元素在列表中出现的次数
# li = ['韩信', '澜', '百里', '马超', '澜', '澜']
# print(li.count('韩信'))


# 列表.index(需要查看的元素)
# 查看最小索引
# print(li.index('澜'))


# sort 和 reverse
# 语法：列表.sort()  将列表进行排序，排序为从小到大
# li = [4, 1, 2, 8, 7]
# li.sort()
# print(li)
# 列表.reverse()  将列表的元素进行反转
# li.reverse()
# print(li)
# 将列表从大到小进行排序
# li.sort()
# li.reverse()
# print(li)
# li.sort(reverse=True)
# print(li)


li = [4, 1, 2, 8]
# 语法：max(列表) 返回列表中的最大值
# print(max(li))
# 语法：min(列表) 返回列表中的最小值
# print(min(li))


# 语法：len(列表)  返回列表里面元素的个数
print(len(li))
