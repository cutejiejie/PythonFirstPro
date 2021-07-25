def fib(n):
    if n==1 or n==2:
        return 1
    else:
        res = fib(n - 1) + fib(n - 2)
        return res
for i in range(1,7):
    print(fib(i))