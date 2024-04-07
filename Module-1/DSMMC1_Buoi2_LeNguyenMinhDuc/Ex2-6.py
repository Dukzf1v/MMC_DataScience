
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    fib_prev = 1
    fib_curr = 1
    for _ in range(3, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
    return fib_curr

n = int(input("Enter n: "))
print("So fibonacci thu n:", fib(n))