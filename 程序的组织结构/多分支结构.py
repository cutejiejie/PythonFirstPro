score = int(input('请输入您的分数:'))
if  90<=score<=100:
    print('A')
elif 80<=score<90:
    print('B')
elif score>=70 and score<80:
    print('C')
elif score>=60 and score<70:
    print('D')
# elif score<=60:
else:
    print('不合格')