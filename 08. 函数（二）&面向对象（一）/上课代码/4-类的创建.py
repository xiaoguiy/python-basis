# 煮菜：买菜、洗菜、放油、下菜、炒
# 面向过程：买菜、洗菜
# 面向对象：创建几个对象，分别让他们取做菜做饭


"""
学生：
属性（特点）：
姓名
年龄
方法（行为）：
学习
做家务
"""


"""
：实现以下操作
创建类：学生类
创建对象：张三
在类中定义方法输出：张三学习Python
"""


# 创建一个学生类
# class Student:
#
#     def student(self):
#         print(self)
#         print('张三学习python')


# 哪个对象调用的方法，self代表的就是哪个对象
# 创建一个张三对象
# zhangsan = Student()
# zhangsan.student()
# print(zhangsan)
#
# print('------------------------------------')
# 创建一个李四对象
# lisi = Student()
# lisi.student()
# print(lisi)


# 创建一个学生类
class Student:

    def info(self):
        print(f'{Tom.name}今年{Tom.age}岁')
        print(f'{self.name}今年{self.age}岁')


Tom = Student()
# 赋值对象的属性
Tom.name = 'Tom'
Tom.age = 18
Tom.info()
