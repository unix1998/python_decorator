class Person(object):   # 定义一个父类
 
    def talk(self):    # 父类中的方法
        print("person is talking....")  
 
 
class Chinese(Person):    # 定义一个子类， 继承Person类
 
    def walk(self):      # 在子类中定义其自身的方法
        print('is walking...')
class Beijing(Chinese):
    def live(self):
       print ('live in Beijin')
 
c = Beijing()
c.talk()      # 调用继承的Person类的方法
c.walk()     # 调用本身的方法
c.live()

