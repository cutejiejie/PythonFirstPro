# （1）% 占位符
name='张三'
age=20
print('我叫%s,今年%d岁' % (name,age))

# （2）{}
print('我叫{0},今年{1}岁'.format(name,age))

# （3）f-string
print(f'我叫{name},今年{age}岁')

print('%10d' % 99) #10表示的是宽度
print('%.3f' % 3.1415926) #.3表示是小数点后三位
print('%10.3f' % 3.1415926) #同时表示宽度和精度,一共总宽度为10，小数点后三位
print('hellohello')

print('--------------------------')
print('{0:.3}'.format(3.1415926)) #.3表示的是一共3位数
print('{:.3f}'.format(3.1415926)) #.3f表示是三位小数
print('{:10.3f}'.format(3.1415926)) #同时设置宽度和精度，一共是10位，3位是小数
print('hellohello')