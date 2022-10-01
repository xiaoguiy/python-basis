file = open('info.txt', mode='r', encoding='utf-8')
# print(file.readable())
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readlines())
# 读的时候 中文字占3个位置  换行符\n占2个位置  普通的英文字符和数字占1个位置
# print(file.tell())  # 0
# print(file.readline())  # hello\n
# print(file.tell())  # 7
# print(file.readline())  # world\n
# print(file.tell())  # 14
# print(file.readline())  # 你好
# print(file.tell())  # 20

