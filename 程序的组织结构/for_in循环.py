# for item in 'jiejieLOVEstudy':
#     print(item)
# for num in range(1,10):
#     print(num)
# for _ in range(1,6):
#     print('jiejieLOVEstudy')

# sum=0
# for num in range(0,101,2):
#     # print(num)
#     sum+=num
# print('0到100之间的偶数和为',sum)

# print('使用for循环，计算1到100之间的偶数和')
# sum=0 #用于存储偶数和
# for item in range(1,100):
#     if item%2==0:
#         sum+=item
# print('1到100之间的偶数和为',sum)

'''
100到999之间的水仙花数
'''
# for num in range(100,1000):
#     a=num//100
#     b=(num-a*100)//10
#     c=num%10
#     if num==a**3+b**3+c**3:
#        print(num,'是水仙花数')

for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    if ge**3+shi**3+bai**3==item:
        print(item)




