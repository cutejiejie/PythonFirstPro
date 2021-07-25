lst=[10,20,30,40,50,60,70,80]
# start=1,stop=6,step=1
# print(lst[1:6:1])
'''
print('原列表:',id(lst))
lst2=lst[1:6:1]
print('切的片段:',id(lst2))
print(lst[1:6]) # 默认步长为1
print(lst[1:6:])
# stop=6,step=2,start采用默认
print(lst[:6:2])
# start=1,step=2,stop采用默认
print(lst[1::2])
'''
# [:stop:step],切片的第一个元素默认是列表的最后一个元素，从start开始往前计算切片
# [start::],切片的最后一个元素默认是列表的第一个元素，从start开始往前计算切片
print(lst[:0:-3])
print(lst[5::-3])
print('------------step步长为负数的情况--------------')
print('原列表:',lst)
print(lst[::-1])
print(lst[7::-1])
print(lst[6:0:-2]) # 不包括0
print(lst[0:6:2])
