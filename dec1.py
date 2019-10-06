# dec.py
from time import time
def timer(func):
  def f(x, y=10):
    before = time()
    rv = func(x, y)
    after = time()
    print('time taken: ', after - before)
    return rv
  return f

def add(x, y=10):
  return x + y
add_1 = timer(add)


def sub(x, y=10):
  return x - y
sub_1 = timer(sub)

print('add_1(10)',         add_1(10))
print('add("a", "b")',   add("a", "b"))
print('sub_1(10)',         sub_1(10))
print('sub(20, 30)',     sub(20, 30))
