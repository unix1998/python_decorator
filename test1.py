def func(name):
    print('我是{}！慌的一逼！'.format(name))
func('梅西')
y = func

y('勒夫')


func('test func origin')
y('test y be assigned as func')

aa = func

aa('test new aa')
