class A:
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, b, c):
        self.b = b
        self.c = c
        super().__init__(c + b)

    def printv(self):
        print(self.a)


b = B(4, 5)
print(b.__dict__)
print(b.a)
print(A.__init__(b, 6))


def add(x: int, y: int) -> int:
    """
    """
    pass
