class Point:  # Point 是引用，是一个标识符，他引用了一个类对象

    def __init__(self, x, y):  # __int__ 也是一个引用，一个标识符，引用了一个函数对象。一种是等价形式，还有key-value形式。
        self.x = x  # ’x'是一个标识符，是一个引用，引用了一个对象，可能是int，可能是str.
        self.y = y

    def show(self):  # show 也是一个标识符，是一个引用，引用了一个函数对象
        print(self.x, self.y)

    def __str__(self):
        print('+++++')
        # print(self.x,self.y)
        return 'P({},{})'.format(self.x, self.y)

    def __getattr__(self, item):
        print('++++getattr++++')
        return 'abc'

    # __setattr__不会自动把属性添加到__dict__中。
    def __setattr__(self, key, value):
        print('+++++setattr++++')
        print('k = {},value={}'.format(key, value))
        self.__dict__[key] = value


p = Point(4, 5)
# print(p.x)
# print(p.y)
p.z = 100
p.__dict__['u'] = 200
print(p.__dict__)
