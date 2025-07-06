def decorate_args(func):
   def wrapped(*args, **kwargs):
       new_args = list(x * 2 for x in args)
       return func(*new_args, **kwargs)
   return wrapped


@decorate_args
def test(a, b):
   return a + b

print(test(5, 8))