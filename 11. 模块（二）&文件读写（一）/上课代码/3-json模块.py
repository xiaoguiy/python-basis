import json
# a = "张三"
# print(type(a))  # <class 'str'>
# b = {"name": "tom"}
# print(type(b))
# c = '{"name": "tom"}'  # json数据的标准格式
# print(type(c))
# json数据的标准：
# 1、最外层得用单引号包裹
# 2、引号里面的内容得以键值对的形式存在
# 3、键值对的键部分必须得用双引号包裹
# 4、键值对的值部分如果是字符串那也得用双引号包裹


# json转字典
# json_data = '{"name": "tom"}'
# 强转
# dic = dict(json_data)
# print(type(dic))
# dic = json.loads(json_data)
# print(type(dic))


# 字典转json
dic = {'name': 'tom'}
# data = str(dic)
# print(data)
# print(type(data))
data = json.dumps(dic)
print(data)
print(type(data))
