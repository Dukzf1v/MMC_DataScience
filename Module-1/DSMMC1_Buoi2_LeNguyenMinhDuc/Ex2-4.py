def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_list(n):
    i = 2
    count = 0
    while count != n:
        if check_prime(i):
            print(i)
            count += 1
        i += 1

n = int(input("Enter n:"))
prime_list(n)
