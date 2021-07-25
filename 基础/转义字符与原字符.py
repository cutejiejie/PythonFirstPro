# 转义字符
# \ +转义功能的首字母 n-->newline的首字符表示换行
print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld') #world将hello进行覆盖
print('hello\bworld') #\b是退一个格，将o退没了

print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')

# 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r,或R
print(r'hello\nworld')
# 注意事项，最后一个字符不能是反斜杠
print(r'hello\nworld\\')

print(chr(0b100111001011000))
print(ord('乘'))