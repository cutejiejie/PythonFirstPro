for row in range(1,10): #行数
    for col in range(1,row+1):
        print(row,'*',col,'=',row*col,end='\t') #不换行输出
    print('') #换行