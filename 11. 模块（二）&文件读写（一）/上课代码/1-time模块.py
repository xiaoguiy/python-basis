import time
import datetime


# print('-------------')
# time.sleep(3)
# print('-------------')


# 从1970年的1月1日的凌晨到现在的秒数
# print(time.time())


# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# 第一个datatime是模块 第二个是类名 第三个就是一个方法
# print(datetime.datetime.now())
# 获取当前时间，并计算出七天前这个时间点的时间
# 获取当前的时间
print(datetime.datetime.now())
print(datetime.datetime.now()-datetime.timedelta(days=7))
