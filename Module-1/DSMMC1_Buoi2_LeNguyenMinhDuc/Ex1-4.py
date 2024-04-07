a = int(input("Nhap so thu nhat:"))
b = int(input("Nhap so thu hai:"))

n = a - b
if (n > 0):
    print("So thu nhat lon hon so thu hai")
elif (n < 0):
    print("So thu nhat nho hon so thu hai")
else:
    print("So thu nhat bang so thu hai")