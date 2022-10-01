# # 定义一个父类
# class Father(object):
#     # 钱方法
#     def money(self):
#         print('爸爸有钱')
#
#
# # 儿子类
# class Son(Father):
#     pass
#     # def money(self):
#     #     print('儿子有钱')
#     #     super().money()
#
#
# # 创建一个儿子对象
# s = Son()
# s.money()


# 多继承
# 定义一个爷爷类
# class GrandFather(object):
#     pass
#     # def money(self):
#     #     print('爷爷有钱')
#
#
# # 定义一个父类
# class Father(GrandFather):
#     # 钱方法
#     pass
#     # def money(self):
#     #     print('爸爸有钱')
#
#
# # 定义一个母亲类
# class Mother(object):
#     # pass
#     # 钱方法
#     def money(self):
#         print('妈妈有钱')
#
#
# # 儿子类
# class Son(Father, Mother):
#     pass
#
#
# # 创建一个儿子对象
# s = Son()
# s.money()
# 情况一
# 子类同时继承了多个父类并且存在同名方法，调用的时候，顺序为从左往右进行寻找
# 如果第一个父类没有找到才去第二个父类里面去找


# 情况二：
# 子类同时继承多个父类并且存在同名方法，且其中父类存在父类，但是，父类的父类不同
# 调用的时候依旧是从左往右进行寻找， 如果第一个父类没有找到，会去第一个父类的父类
# 里面去找，如果还找不到才去第二个父类去找


# class GrandFather(object):
#     def money(self):
#         print('爷爷有钱')
#
#
# class Father(GrandFather):
#     # pass
#     def money(self):
#         print('爸爸有钱')
#
#
# # 姑姑
# class Aunt(GrandFather):
#     pass
#
#
# # 儿子类
# class Son(Aunt, Father):
#     pass
#
#
# s = Son()
# s.money()
# 情况三
# 当子类同时继承了多个父类，并且父类的父类相同，存在同名方法时，调用顺序从左往右
# 当第一个父类没有的时候会去第二个父类里面去找，如果都没有才去父类的父类里面去找


# 继承的拓展
class Father:
    def money(self):
        print(self)
        print('爸爸有钱钱')


class Mother:
    def house(self):
        print('妈妈有房')


class Son(Mother, Father):
    def study(self):
        print('学习python')
        # 方法如果自带self参数，那就必须得是对象调用，否则不会默认传入对象
        Father.money(self)


s = Son()
s.study()
print(s)
