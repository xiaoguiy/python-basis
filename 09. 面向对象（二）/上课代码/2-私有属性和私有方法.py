class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 只能返回字符串
    def __str__(self):
        return f'{self.name}今年{self.__age}岁'

    # 打印信息
    def __info(self):
        print(self.name, self.__age)

    def get_age(self):
        return self.__age

    def get_info(self):
        self.__info()


# 创建一个对象
tom = Student('Tom', 18)
# print(tom.__age)  # AttributeError: 'Student' object has no attribute '__age'
# tom.info()
# age = tom.get_age()
# print(age)
# tom.__info()  # AttributeError: 'Student' object has no attribute '__info'
tom.get_info()
