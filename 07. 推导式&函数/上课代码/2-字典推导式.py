# eg1：将列表 li 中的元素，每个都实现小写与大写的映射。如：{"name":"NAME"}
#
# li = ["name", "age", "gender"]
# 字典推导式一
# 语法：{键:值 for 变量 in 序列}
# 创建一个空字典用于存储
# dic = {}
#
# dic[新键] = 新值
# li = ["name", "age", "gender"]
# for i in li:
#     dic[i] = i.upper()
# print(dic)
# dic = {i: i.upper() for i in li}
# print(dic)


# eg2：创建字典 all_stu = {“牛牛”:98, “张三”:40, “老王”:50, “小红”:88, “小明”:79} 保存学生姓名与成绩。
#
# 需求：取出班级成绩不及格 (<60) 的学生的姓名与成绩(字典)
# 创建一个空字典存储目标值
# dic_result = {}
dic = {'张三': 90, '李四': 40, '王麻子': 30}
# for i in dic.keys():
#     if dic[i] < 60:
#         dic_result[i] = dic[i]
# print(dic_result)


# 字典推导式二
# 语法：{键:值 for 变量 in 序列 if 条件}
# dic = {i: dic[i] for i in dic.keys() if dic[i] < 60}
# print(dic)
