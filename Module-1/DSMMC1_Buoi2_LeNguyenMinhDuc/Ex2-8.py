n = int(input("Enter number:"))
original_n = n
sum_digits = 0

while n != 0:
    sum_digits += n % 10
    n //= 10  

print("Sum digits: ", sum_digits)

n = original_n 

my_list = [] 

while n > 1:
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0:
            my_list.append(i)
            n //= i
            break
    else:
        my_list.append(n)
        break

for element in my_list:
    print(element, "*", end=" ")
print("\b\b ")
