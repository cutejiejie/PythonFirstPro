money = 1000
s = int(input('请输入取款金额'))
if s <= 1000:
    money = money - s
    print('您的余额为：' ,money)