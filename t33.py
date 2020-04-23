# 一套方法，不同表现，不同子类继承父类的同一种方法，但是各自实现方式不一样。

class Mixin:

    def show(self):
        print('show')

    def add(self):
        print('++add+++')


class Mixin1:

    def hello(self):
        print('hello')

    def world(self):
        print('world')


class A(Mixin, Mixin1):
    pass


a = A()
print(A.mro())
print(a.show())
print(a.hello())
