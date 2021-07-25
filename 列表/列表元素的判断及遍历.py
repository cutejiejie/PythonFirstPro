print('P' in 'Python')
print('k' not in 'Python')

lst=[10,20,'Python','hello']
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)
print('-------------------')
'''
for 迭代变量 in 列表名：
可迭代变量目前学到的有字符串、列表
'''
for item in lst:
    print(item)