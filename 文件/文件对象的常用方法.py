'''
file=open('a.txt','r')
# print(file.readlines())
# print(file.read(4))
print(file.readline())
file.close()
'''

'''
file=open('c.txt','a')
# file.write('hello')
lst=['java','go','python']
file.writelines(lst)
file.close()
'''

# file=open('a.txt','r')
# file.seek(2)
# print(file.read())
# print(file.tell())
# file.close()

file=open('d.txt','a')
file.write('Hello')
# file.close()
file.flush()
file.write('World')