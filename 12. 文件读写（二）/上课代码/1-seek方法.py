# w或者a模式如果如果文件不存在会创建一个，r模式不存在会报错
# file = open('data.txt', mode='w')
# file.write('hello\nworld\n你好')


# file = open('data1.txt', mode='r')
# print(file.tell())
# print(file.read())
# print(file.tell())
# print('------')
# print(file.read())
# print(file.seek())


# offset：偏移量
# whence：指针对位置：0起始位置  1当前位置  2结尾的位置  默认为0
# print(file.tell())
# file.seek(9, 0)
# print(file.tell())  # 9
# file.seek(1, 1)
# print(file.tell())
# print(file.read())
# file.seek(1, 1)
# print(file.read())


# b 二进制模式 才能把指针放到当前或者结束位置
# 普通的模式只能放到开头
file = open('data1.txt', mode='rb')
print(file.tell())  # 0
file.seek(5, 0)
print(file.tell())  # 5
file.seek(1, 1)
print(file.tell())
