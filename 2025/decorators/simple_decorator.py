def decorate(func):
   def wrapped(*args, **kwargs):
       print('Call function {} with arguments:'.format(func.__name__), args)
       return func(*args, **kwargs)
   return wrapped


@decorate
def test(a, b):
    return a + b

print(test(5, 8))