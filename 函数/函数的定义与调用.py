'''a,b称为形式参数，简称形参，形参的位置是在函数定义处'''
def calc(a,b):
    c=a+b
    return c

'''10,20称为实际参数的值，简称实参，实参的位置是在函数的调用处'''
result=calc(10,20)
print(result)

'''=左侧的变量的名称为关键字参数'''
res=calc(b=10,a=20)
print(res)