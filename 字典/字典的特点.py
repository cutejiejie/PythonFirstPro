# key不允许重复
d={'name':'张三','name':'李四'}
print(d)

# value可以重复
d={'name':'张三','nikename':'张三'}
print(d)

lst=[10,20,30]
lst.insert(1,100)
print(lst)
d={lst:100}
print(d)
