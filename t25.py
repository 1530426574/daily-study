class Dispatcher:
    def __init__(self):
        pass

    def reg(self, name, fn):
        setattr(self, name, fn)

    def run(self):
        while True:
            cmd = input('>>>').strip()
            if cmd == 'quit':
                break
            # 关键在哪呢，在getattr返回的是什么，是name引用的对象，即我们真正想要的是self.cmd,
            # 和我么打印print(d)本质是一样的，d引用了一个对象
            getattr(self, cmd, lambda: print('unknown cmd {}'.format(cmd)))()


d = Dispatcher()
d.reg('show', lambda: print('show'))
d.reg('add', lambda: print('add'))
print(d.__dict__)
d.run()
