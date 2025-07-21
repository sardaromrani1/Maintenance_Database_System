from decorators.decorators import cache_query
import time

@cache_query(timeout=10)
def add(a, b):
    print("Calculating ...")
    return a+b

print(add(2, 3))
print(add(2, 3))

time.sleep(8)
print(add(2, 3))