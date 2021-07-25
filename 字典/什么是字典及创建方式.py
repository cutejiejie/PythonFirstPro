'''
工序:hash(key)计算存储位置，
所以要求放在字典当中的键必须是一个不可变序列：字符串str、整数序列
可变序列：列表、字典
'''
'''使用{}创建字典'''
scores={'张三':100, '李四':98, '王五':45}
print(scores)
print(type(scores))

'''第二种创建dict()'''
student=dict(name='jack', age=20)
print(student)
print(type(student))

'''空字典'''
d={}
print(d)
print(type(d))