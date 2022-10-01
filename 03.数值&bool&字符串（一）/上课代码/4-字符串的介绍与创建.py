# 单引号
s1 = 'he' \
     'llo'
# print(s1)  # hello
# 双引号
s2 = "he" \
     "llo"
# print(s2)  # hello
# 三引号创建的多行字符会保留文本的原有格式，而单引号和双引号不行
s3 = '''hello



# 中文的引号： “ ”
# 英文的引号： " "



world
'''
print(s3)