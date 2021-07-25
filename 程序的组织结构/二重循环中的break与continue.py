# for i in range(5):
#     for j in range(1,11):
#         if j%2==0:
#             break
#         print(j,'第',i,'次')

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()