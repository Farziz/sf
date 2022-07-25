def decorator(func):
    def inner(*args):
        print('start')
        print('finished')
        return func(*args)
    return inner

def func(*args):
    return sum(args)

a = decorator(func)
print(a(9,3,3))

print(func(9,3,3))

@decorator
def func1(*args):
    return sum(args)*2

print(func1(9,3,3))
    
    
    
    
    
    
    
print(func1(9,3,3))



print(func1(9,3,3))