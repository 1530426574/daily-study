# 反射，对象在内存中运行的时候，可以获取其类型信息。
# 查看对象属性，对象属性放在哪呢，在__dict__中，有哪些方式访问呢
class Point(object):  # Point 是引用，是一个标识符，他引用了一个类对象

    def __init__(self, x, y):  # __int__ 也是一个引用，一个标识符，引用了一个函数对象。一种是等价形式，还有key-value形式。
        self.x = x  # ’x'是一个标识符，是一个引用，引用了一个对象，可能是int，可能是str.
        self.y = y

    def show(self):  # show 也是一个标识符，是一个引用，引用了一个函数对象
        print(self.x, self.y)

    def __str__(self):
        print('+++++')
        # print(self.x,self.y)
        return 'P({},{})'.format(self.x, self.y)


p = Point(4, 5)
print(p)
print(p.show())
print(p.__dict__)
p.__dict__['z'] = 6
print(p.__dict__)
p.z = 10
print(p.__dict__)
p.u = 100
print(p.__dict__)
print(dir(p))
print(p.__dir__())
print(p.__dict__.get('a'))
print(1, getattr(p, 'a', 'b'))
print(2, hasattr(p, 'a'))
setattr(p, 'x', 100)
print(p.__dict__)
if hasattr(p, 'x'):
    print('=============')
    print(p.x)
    setattr(Point, 'add', lambda x, y: x + y)
    print(3, Point.__dict__)

print(4, globals())
# 模块
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000026D4E134C18>, '__spec__': None, '__annotations__': {},
# '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/Users/Yamu.com/PycharmProjects/daily-study/t24.py', '__cached__': None,
# 'Point': <class '__main__.Point'>, 'p': <__main__.Point object at 0x0000026D4E214E80>}
# 类
# {'__module__': '__main__',
# '__init__': <function Point.__init__ at 0x000001A7619A51E0>,
# 'show': <function Point.show at 0x000001A7619A5598>,
# '__str__': <function Point.__str__ at 0x000001A7619A5620>,
# '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None,
# 'add': <function <lambda> at 0x000001A7619A5268>}
# 实例
# {'x': 4, 'y': 5, 'z': 6}
# 本质是什么呢？赋值即定义，x = 1,最后以key:value 的 形式保存在对象字典中，关键key为字符串
