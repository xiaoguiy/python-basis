# __init__:对象创建成功之后自动调用
# class Student(object):
#     def __init__(self):
#         print('__init__')
#
#     def __new__(cls, *args, **kwargs):
#         print('__new__')
#         return super().__new__(cls)
#
#
# tom = Student()
# 创建对象的过程
# 1、tom = Student()告诉程序需要创建一个对象
# 2、调用new方法创建一个对象并返回出去
# 3、系统自动将对象传入init方法
# 4、如果init接收到了对象则执行，没有接收到则不执行，也就是说对象创建成功并返回才会调用


class Student:

    def __del__(self):  # delete
        print('对象删除成功')


tom = Student()
del tom
print('hello')

