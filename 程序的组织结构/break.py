# a=0
# while a<3:
#     '''条件执行体（循环体）'''
#     pwd=input('请输入密码:')
#     if pwd=='8888':
#         print('密码正确')
#         break
#     else:
#         print('密码不正确')
#     '''改变变量'''
#     a+=1

for item in range(3):
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')