class Animal:

    def __init__(self, name):
        self.__name = name

    def shout(self):
        print(self, 'shout')

    @property
    def name(self):
        return self.__name


a = Animal('CAT')
print(a.name)
a.shout()


class Dog(Animal):
    pass


d = Dog('小王')
print(d.name)
d.shout()
print(d.__dict__)  # {'_Animal__name': '小王'}
# print(d.__class__.__base__)
# print(Animal.__base__)
# print(Dog.__bases__)
# print(Dog.__mro__)
# print(Dog.mro())
# print(object.__subclasses__())
