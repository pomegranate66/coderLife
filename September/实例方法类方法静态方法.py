class Kls(object):
    def foo(self, x):
        print('executing foo(%s,%s)' % (self, x))

    @classmethod
    def class_foo(cls,x):
        print('executing class_foo(%s,%s)' % (cls,x))

    @staticmethod
    def static_foo(x):
        print('executing static_foo(%s)' % x)

ik = Kls()

# 实例方法
ik.foo(1)
# print(ik.foo)
print('==========================================')

# 类方法
ik.class_foo(1)
Kls.class_foo(1)
# print(ik.class_foo)
print('==========================================')

# 静态方法
ik.static_foo(1)
Kls.static_foo('hi')
# print(ik.static_foo)

# 输出
# executing foo(<__main__.Kls object at 0x0000027237209EC8>,1)
# ==========================================
# executing class_foo(<class '__main__.Kls'>,1)
# executing class_foo(<class '__main__.Kls'>,1)
# ==========================================
# executing static_foo(1)
# executing static_foo(hi)