import math

def check_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number: "))
for i in range(2, n):
    if check_prime(i):
        print(i)

