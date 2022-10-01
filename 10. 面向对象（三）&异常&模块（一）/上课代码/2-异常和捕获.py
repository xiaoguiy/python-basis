# n = input('请输入一个数字')
# num = float(n)
# print(num)
# print('hello world')


# try:
#     n = input('请输入一个数字')
#     num = float(n)
#     print(num)
#     print('hello world')
# except ValueError as e:
#     print(e)
#     num = 1
#     print(num)


# li = [1, 2, 3]
# print(li[7])
# try:
#     n = input('请输入一个数字')
#     num = float(n)
#     print(num)
#     print('hello world')
# except Exception as e:
#     print(e)


# try:
#     li = [1, 2, 3]
#     print(li[1])
#     print('hello world')
# except Exception as e:
#     print(e)
# else:
#     print('正常执行')
# finally:
#     print('我是你大哥')


# 判断煎饼熟了没，当烹饪时间小于5时，则主动触发没熟异常；否则熟了
# try:
#     # 接收烹饪时间
#     in_time = float(input('请输入烹饪时间：'))
#     if in_time < 5:
#         raise Exception('煎饼还没熟，你猴急啥')
# except Exception as e:
#     print(e)
# else:
#     print('熟了，请使用')


# class S(Exception):
#     pass


# 用户输入一串密码，如果密码长度小于六则抛出异常
# class ShortInputError(Exception):
#     def __str__(self):
#         return '你的密码太短了'
#
#
# try:
#     pwd = input('请输入密码：')
#     if len(pwd) < 6:
#         raise ShortInputError()
#     print(pwd)
# except Exception as e:
#     print(e)

n = 1
assert n > 0
print('你好哇')

