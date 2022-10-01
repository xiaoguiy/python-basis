class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 只能返回字符串
    def __str__(self):
        return f'{self.name}今年{self.age}岁'


# 创建一个对象
tom = Student('Tom', 18)
print(tom)
