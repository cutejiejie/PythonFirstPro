try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第一二个整数'))
    result=a/b
    print('结果为:',result)
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为',result)