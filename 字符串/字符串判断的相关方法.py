s='hello,python'
print('-------isidentifier()判断指定的字符串是不是合法的标识符------')
print('1.',s.isidentifier())
print('2.','hello'.isidentifier())
print('3.','张三_'.isidentifier())
print('4.','张三_123'.isidentifier())

print('------isspace()判断指定的字符串是否全部由空白字符组成（回车、换行、水平制表符）--------')
print('5.','\t'.isspace())

print('--------isalpha()判断指定的字符串是否全部由字母组成---------')
print('6.','abc'.isalpha())
print('7.','张三'.isalpha())
print('8.','张三1'.isalpha())

print('--------isdecimal()判断指定的字符串是否全部由十进制数字组成---------')
print('9.','123'.isdecimal())
print('10.','123四'.isdecimal())
print('11.','IIIIII'.isdecimal())

print('--------isnumeric()判断指定的字符串是否全部由数字组成---------')
print('12.','123'.isnumeric())
print('13.','123四'.isnumeric())
print('14.','ⅢⅢⅢ'.isnumeric())

print('--------isalnum()判断指定的字符串是否全部由字母和数字组成---------')
print('15.','abc1'.isalnum())
print('16.','张三123'.isalnum())
print('17.','abc!'.isalnum())