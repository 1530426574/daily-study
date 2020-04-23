# 多态，不同的子类继承同一方法，但各自实现不一样。
# def add_name(cls,name):
#     cls.NAME = name
import t29

# def add_name(name):
#     def wrapper(cls):
#         cls.NAME = name
#         return cls
#     return wrapper
#
#
# @add_name('name') #MyClass = add_name(name)(MyClass)
# class MyClass:
#
#     hight = 188
#     def __init__(self,name,age):
#         print('++++init+++++')
#         self.name =name
#         self.age = age
#         print(1, self)
#
#     def show(self):
#         print('self = {}'.format(self))
#         print(self.name,self.age)
#
#     def __str__(self):
#         return 'MyClass({},{})'.format(self.name,self.age)

# a= MyClass('louis',18)
# print(a.name,a.age,a.hight)
# print(a.__dict__)
# print(MyClass.__class__,type(MyClass))
# print(a.__class__.__qualname__)
# print(MyClass.age)#实例可以访问类的属性，但类不能访问实例的属性。

a = globals()['t29']
print(1, a, type(a))
print(3, a.__dict__)
