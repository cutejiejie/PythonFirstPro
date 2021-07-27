class Person(object): #Person继承ogject类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name,self.age),end='\t')

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):
        super().info()
        print('学号:{0}'.format(self.stu_no))

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):
        super().info()
        print('教龄:{0}'.format(self.teachofyear))

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)

stu.info()
print('-------------------------')
teacher.info()
