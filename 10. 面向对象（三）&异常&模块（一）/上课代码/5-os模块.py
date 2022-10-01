import os


# 获取当前的工作目录
# print(os.getcwd())
# print(os.chdir('C:'))
# print(os.getcwd())

# 以递归的方式创建多个文件夹
# os.makedirs('顾卿\\db')
# os.removedirs('顾卿\\db')


# 创建单个文件夹
# 如果有嵌套路径，只会创建最后一个文件夹，但是，创建之前会检查前面的文件夹是否存在
# 存在则创建，不存在则报错
# os.mkdir('顾卿\\db')
# os.rmdir('顾卿')
# os.removedirs('顾卿\\db')


# os.mkdir('顾卿')
# print(os.path.exists('顾卿'))
# 现在我就想要创建一个img这个文件夹，但是，我不知道是否存在
# if not os.path.exists('img'):
#     os.mkdir('img')


# 拼接路径
head = '顾卿'
s = 'db'
# 顾卿\db
# print(head+'\\'+s)
print(os.path.join(head, s))
