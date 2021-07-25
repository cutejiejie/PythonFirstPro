# for num in range(1,51):
#     if num%5==0:
#         print(num)

for item in range(1,51):
    if item%5!=0:
        # print('不是5的倍数的有:',item)
        continue
    print(item)