
def add(x, y=10):
  return x + y
add = timer(add)

@timer
def add(x, y=10):
  return x + y

print (add(5))
