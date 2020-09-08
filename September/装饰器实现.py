# 字体变粗装饰器
import datetime
from time import sleep


def makebold(fn):
    # 装饰器将返回新的函数
    def wrapper(*args, **kwargs):
        # 在之前或者之后插入新的代码
        print(args)
        print(kwargs)
        print("starttime:{}".format(datetime.datetime.now()))
        fn(*args, **kwargs)
        print("endtime:{}".format(datetime.datetime.now()))
        # return fn(*args,**kwargs)

    return wrapper


@makebold
def fun(s, a):
    print(s)
    for i in range(10):
        print(i)
    print(a)


fun(s=["hahah"], a={'a': 1, 'b': 2})

# 输出: <b><i>hello</i></b>
