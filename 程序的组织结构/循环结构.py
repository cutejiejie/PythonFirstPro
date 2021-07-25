# a=1
# while a<10:
#     print(a)
#     a+=1

# while是判断N+1次，条件为True执行N次
'''
4步循环发
1.初始化变量
2.条件判断
3.条件执行体（循环体）
4.改变变量
总结：初始化的变量与条件判断的变量与改变的变量为同一个
'''

'''
a=3
b=8
num=a
while a<b:
    a+=1
    num+=a
print(num)
'''


# sum=0 # 用于存储累加和
# '''初始化变量为0'''
# a=0
# '''条件判断'''
# while a<5:
#     '''条件执行体（循环体）'''
#     sum+=a
#     '''改变变量'''
#     a+=1
# print('和为',sum)

a=1
b=100
sum=0
while a<=b:
    if not bool(a%2):
        sum+=a
    a+=1
print(a-100,'与',b,'之间的偶数和为',sum)




