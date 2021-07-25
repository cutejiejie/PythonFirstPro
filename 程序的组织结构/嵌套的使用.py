answer = input('请问您是会员吗，请输入y OR n:')
money = float(input('请输入您消费的金额:'))
if answer == 'y':
    if money >= 200:
        print('您的购物金额为:', money*0.8)
    elif money >=100:
        print('您的购物金额为:', money * 0.9)
    else:
        print('暂无折扣，您的购物金额为:', money)
else:
    if money >= 200:
        print('您的购物金额为:', money * 0.95)
    else:
        print('暂无折扣，您的购物金额为:', money)