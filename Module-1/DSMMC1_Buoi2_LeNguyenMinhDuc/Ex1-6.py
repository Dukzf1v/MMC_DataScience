
math = float(input("Nhap vao diem toan: "))
physic = float(input("Nhap vao diem ly: "))
chemis = float(input("Nhap vao diem hoa: "))


aver = (math * 2 + physic + chemis) / 4

def hoc_luc(aver):
    match aver:
        case _ if aver >= 9.0:
            return "Xuat sac"
        case _ if 8.0 <= aver < 9.0:
            return "Gioi"
        case _ if 7.0 <= aver < 8.0:
            return "Kha"
        case _ if 6.0 <= aver < 7.0:
            return "Trung binh kha"
        case _ if 5.0 <= aver < 6.0:
            return "Trung binh"
        case _:
            return "Kem"

hoc_luc = hoc_luc(aver)


print("Hoc luc cua hoc sinh la:", hoc_luc)
