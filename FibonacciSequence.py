from functools import cache, lru_cache
@cache
def fib(n):
    if n <=1:
        return n
    else:
        return fib(n-2)+fib(n-1)

x = int(input("x:"))
sum = fib(x)
print(sum)