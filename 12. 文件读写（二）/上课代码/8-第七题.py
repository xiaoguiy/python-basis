# 7.往hello.txt的文本文件中写入两行文本 hello,world\nhello,python (使用utf-8编码)


with open('hello.txt', mode='w', encoding='utf-8') as f:
    f.write('hello,world\nhello,python')
