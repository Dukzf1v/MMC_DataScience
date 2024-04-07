def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter n: "))
my_list = []
for i in range(1, n+1):
    if n % i == 0:
        my_list.append(i)

print("Cac uoc so cua ", n, "la:")
for element in my_list:
    print(element, end=" ")

print("\nCac uoc so nguyen to cua ", n, "la:")
for element in my_list:
    if check_prime(element):
        print(element, end=" ")
