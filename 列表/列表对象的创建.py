a=10 #变量存储的是一个对象的引用
'''创建列表的第一种方式，使用[]'''
lst=['hello','world',98]
# print(id(lst))
# print(type(lst))
# print(lst)
'''创建列表的第二种方式，使用内置函数list()'''
lst2=list(['hellojiejie','world',18,'jiejieBSL','world'])
# 正向索引从0到N-1
print(lst2[4])
# 逆向索引从-N到-1
print(lst2[-5])
# 如果列表中有相同元素只返回列表中相同元素的第一个元素的索引
print(lst2.index('world'))
# print(lst2.index('world'))
print(lst2.index(18,2,3))