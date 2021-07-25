lst=[10,20,30,40,50,60,30]
lst.remove(30) # 从列表中移除一个元素，如果有重复元素值移第一个元素
print(lst)

# pop()根据索引移除元素
lst.pop(1)
print(lst)

# lst.pop(5)
# print(lst)

lst.pop()
print(lst)

print('-----------切片操作-删除至少一个元素，将产生一个新的列表对象----------')
new_list=lst[1:3]
print('原列表',lst)
print('切片后的列表',new_list)

'''不产生新的列表对象，而是删除原列表中的内容'''
lst[1:3]=[]
print(lst)

'''清除列表中的所有元素'''
lst.clear()
print(lst)

'''del语句将列表对象删除'''
# del lst
# print(lst)