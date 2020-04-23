class Person:

    def __init__(self, name, age=19):
        self.name = name
        self.__age = age

    @property
    def age(self):
        print('++++++++++++age=======')
        return self.__age

    @age.setter
    def age(self, age):
        print('===settter')
        self.__age = age

    @age.deleter
    def age(self):
        print('del')


p = Person('louis')
print(p.__dict__)
print(p.age)
print(Person.__dict__.keys())
p.age = 80
print(p.age)
print(p.__dict__)
