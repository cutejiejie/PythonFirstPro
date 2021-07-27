'''
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动')

car=Car('宝马X5...')
car.start()
print(car.brand)
'''

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  #年龄不希望在类的外部被使用，所以加了两个_
    def show(self):
        print('我是'+self.name+',今年',self.__age,'岁了')
stu=Student('张三',20)
stu.show()
# 在类外使用name与age
print(stu.name)
# print(stu.__age)
# print(dir(stu))
print(stu._Student__age)