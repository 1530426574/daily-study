class Person:

    # 对象有很多属性，属性对应着不同类型的对象。

    def __init__(self, name, age):
        self.name = name
        self._age = age

    def _get(self):
        pass

    def __get1(self):
        pass

    class A:
        pass

    @classmethod
    def show(cls):
        print('+++++++++++++++++++++++')
        print('cls={}'.format(cls))
        cls.NAME = 'louis'

    @staticmethod
    def add():
        print('---add----')

    def show_age(self):
        return self._age


print(Person.__dict__)
# 不管是哪种方法，都属于类的属性，当然也是该类实例的属性；
# 方法和方法的调用，与方法后面要求的参数相关。
#
# a = Person('louis',18)
#
# print(a.show_age())
# print(a.__dict__)
# print(a._age)
