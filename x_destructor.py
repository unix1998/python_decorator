class Test(object):
    def __init__(self, name):
        self.name = name
        print('这是构造函数')
 
    def say_hi(self):
        print('hell, %s' % self.name)
 
    def __del__(self):
        print('这是析构函数')
        print ('test1234')
 
obj1 = Test('bigberg')
 
obj1.say_hi()
 
del obj1
