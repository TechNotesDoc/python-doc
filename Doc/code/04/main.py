# 类装饰器
class CounterDecorator:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Function has been called {self.count} times")
        return self.func(*args, **kwargs)

@CounterDecorator
def multiply(a, b):
    return a * b

result = multiply(2, 3)
print(result)
result = multiply(4, 5)
print(result)