# is  和   == 的区别
# is 比较的是内存地址是否一样
# == 比较的是内存里面的值是否一样


a = 10000
b = 10000
print(a is b)  # False
print(a == b)  # True