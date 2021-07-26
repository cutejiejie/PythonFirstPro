class Student:
    native_pace='吉林' #直接写在类里的变量，称为类属性
    def __init__(self,name,age): #name,age为实例属性
        self.name=name #self.name称为实体属性，进行了一个赋值操作，将局部变量的name的值赋给实体属性
        self.age=age

    # 实例方法
    def eat(self):
        print('学生在吃饭...')

    # 静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    # 类方法
    @classmethod
    def cl(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

# 在类之外定义的称为函数，在类之内定义的称为方法
def drink():
    print('喝水')

# 创建Student类的对象
stu1=Student('张三',20)
# print(id(stu1))
# print(type(stu1))
# print(stu1)
stu1.eat()  #对象名.方法名（）
print(stu1.name)
print(stu1.age)

print('-----------------------')
Student.eat(stu1) #35行与30行代码功能相同，都是调用Student中的eat方法
                  #类名.方法名（类的对象）-->实际上就是方法定义处的self
