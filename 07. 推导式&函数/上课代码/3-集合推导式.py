# eg1：随机生成 10 个 1-100 之间的元素，并且去重。
import random
# print(random.randint(1, 10))
# randint这个方法的两边都是可以去得到的
# 语法：{需要放到里面的元素 for 变量 in 序列}
# 创建一个空的集合
# s = set()
# for i in range(1, 11):
#     s.add(random.randint(1, 100))
# print(s)
# s = {random.randint(1, 100) for i in range(1, 11)}
# print(s)

# 元组没有推导式
# tup = (i for i in range(1, 11))
# print(tup)  # <generator object <genexpr> at 0x00000228F05DA548>
