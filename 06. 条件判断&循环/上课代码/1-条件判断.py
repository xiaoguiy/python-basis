# eg1：用户输入姓名以及性别
# 当性别为女时，输出"邀请**女士参加20220316晚上的联谊会！"
# 否则，男生已满，欢迎下次再来。


name = input('请输入姓名：')
sex = input('请输入性别：')
# 单分支
# if sex == '女':
#     print(f'邀请{name}女士参加20220316晚上的联谊会！')
# else:
#     print('男生已满，欢迎下次再来。')


# 多分支
if sex == '女':
    # print(f'邀请{name}女士参加20220316晚上的联谊会！')
    is_marry = input('请输入是否有对象（是/否）：')
    if is_marry == '是':
        print('请分手后再来')
    else:
        print(f'邀请{name}女士参加20220316晚上的联谊会！')
elif sex == '男':
    print('男生已满，欢迎下次再来')
elif sex == '人妖':
    pass
else:
    print('您输入有误无法识别')