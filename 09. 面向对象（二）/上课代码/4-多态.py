# 定义：相同的方法以不同的方式实现
# 发生前提：
# 1、存在继承
# 2、发生子类重写父类方法


class People:
    def work(self):
        pass


# 程序员
class ChengXuYuan(People):
    def work(self):
        print('程序员代码')


# 厨师
class ChuShi(People):
    def work(self):
        print('厨师煮菜')


# 厨师
cx = ChuShi()
# 程序员
csx = ChengXuYuan()
cx.work()
csx.work()
