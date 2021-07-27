# encoding:utf-8
from datetime import datetime



def catch_exception(origin_func):
    def wrapper(self, *args, **kwargs):
        try:
            print ("begin")
            origin_func(self, *args, **kwargs)
            print ("end")
        except Exception:
            self.revive() #不用顾虑，直接调用原来的类的方法
            return 'an Exception raised.'
    return wrapper

class Test(object):
    def __init__(self):
        pass

    def revive(self):
        print('revive from exception.')
        # do something to restore

    @catch_exception
    def read_value(self):
        print('here I will do something.')
        # do something.

test = Test()
test.read_value()
