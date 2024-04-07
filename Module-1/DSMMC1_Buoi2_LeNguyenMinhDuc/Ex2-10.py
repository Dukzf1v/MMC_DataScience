def Chuan_hoa(s):
    s = ' '.join(s.split())

    s = s.title()

    return s

str = input("Nhap chuoi: ")

Chuan_hoa = Chuan_hoa(str)
print("Chuoi chuan hoa: ", Chuan_hoa)
