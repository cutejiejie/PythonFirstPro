# -*- coding:utf-8 -*-
'''
file=open('a.txt','r')
print(file.readlines())
file.close()
'''

'''
file=open('b.txt','w')
file.write('Python')
file.close()
'''

'''
file=open('b.txt','a')
file.write('Python')
file.close()
'''


src_file=open('旺仔小妹.png','rb')
target_file=open('旺仔小妹复制.png','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()
