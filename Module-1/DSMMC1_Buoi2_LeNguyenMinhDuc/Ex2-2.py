n = int(input("Enter number: "))
my_list = []

while n > 1:
    for i in range(2, n + 1): 
        if n % i == 0:
            my_list.append(i)
            n //= i 
            break

for element in my_list:
    print(element, "*", end=" ")
print("\b\b ")
 
