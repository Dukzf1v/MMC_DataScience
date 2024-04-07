def gcd(a, b):
    while b:
        temp = a
        a = b
        b = temp % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))

gcd_result = gcd(a, b)  
lcm_result = lcm(a, b)  

print("GCD: ", gcd_result)
print("LCM: ", lcm_result)