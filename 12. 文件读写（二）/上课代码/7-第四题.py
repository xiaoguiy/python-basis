# 4.创建文件data.txt,文件共100行，每行存放一个1～100之间的整数，最后读取文件里面的值
import random
# print(random.randint(1, 100))
with open('data.txt', mode='w+') as f:
    for i in range(1, 101):
        # 产生随机数
        num = random.randint(1, 100)
        f.write(str(num)+'\n')
        f.seek(0)
        print(f.read())
