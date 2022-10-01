import json
# 将json文件读取为字典
# file = open('hello.json', mode='r')
# data = file.read()
# print(type(data))
# data_dic = dict(data)  # '{"name": "tom"}'
# print(type(data))
# data = json.load(file)
# print(type(data))


# 将字典写入json文件
file = open('hello.json', mode='w')
dic = {'hobby': 'cooking'}
# write只能写入str类型的数据
# data = str(dic)
# file.write(data)
json.dump(dic, file)
