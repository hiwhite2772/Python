diem = float(input("Nhập điểm lần 1 của bạn: "))
if diem >=5:
    diem_moi = diem + 2
else:
    diem_moi = diem + 5
diem_chinh = round(min(diem_moi, 10), 1)
print("Điểm lần 2 của bạn là:", diem_chinh)
