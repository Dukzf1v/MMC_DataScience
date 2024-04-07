n = int(input("Enter n:"))
fact = 1
for i in range(1, n+1):
    fact *= i
print(n,"\b! =", fact)