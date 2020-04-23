class B:
    b = 200


class A(B):
    z = 100
    d = {}

    def __init__(self, x, y):
        self.x = x
        setattr(self, 'y', y)
        self.__dict__['a'] = 5

    def __getattr__(self, item):
        print('++++getattr+++++')
        return self.d[item]

    # 这两个魔术方法的关键在于一个查找对象的属性，一个是为对象添加属性。
    def __setattr__(self, key, value):
        print('++++=setattr++++')
        print('key = {},value={}'.format(key, value))
        self.d[key] = value

    # def __getattribute__(self, item):
    #     print('+++getattribute+++++')
    #     print('item = {}'.format(item))
    #     print(type(item))
    #     print(1,object.__getattribute__(self,item))
    #     return object.__getattribute__(self,item)


a = A(4, 5)
a.x = 5
# print(a.x)
# print(1,a.__dict__)
# print(2,a.d)
# print(3,A.__dict__)
# print(4,a.x)
# print(5,a.y)
# print(6,a.a)
# print(7,a.z)
