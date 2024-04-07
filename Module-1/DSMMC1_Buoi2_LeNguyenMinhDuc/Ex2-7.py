def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fib(n):
    fib_prev = 1
    fib_curr = 1
    fibonacci_list = []
    while fib_curr < n:
        if check_prime(fib_curr):
            fibonacci_list.append(fib_curr)
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
    return fibonacci_list

n = int(input("Enter n: "))
list = fib(n)
print("Cac so nguyen to nho hon", n, "la:", list)
