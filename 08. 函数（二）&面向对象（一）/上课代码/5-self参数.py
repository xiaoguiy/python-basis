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
