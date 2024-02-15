x = int(input("Enter a number of repetitions: "))

def repeat_hello(x):
    def decorator(func):
        def wrapper():
            for _ in range(x):
                func()
        return wrapper
    return decorator

@repeat_hello(x)
def hello():
    print('Hello')

hello()
