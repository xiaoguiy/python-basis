class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, self.age)


lis = Student('李四', 19)
# print(lis.name)
# print(lis.age)
lis.print_info()
tom = Student('tom', 18)
# print(tom.name)
# print(tom.age)
tom.print_info()
