# 注意：一旦用w模式打开里面的东西就被清空了
file = open('info.txt', mode='w', encoding='utf-8')
print(file.writable())
# print(file.write('abc'))
print(file.writelines(['第一行\n', '第二行']))
