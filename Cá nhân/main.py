#1
print("Xin chào mọi người Việt Nam!")
print("1945 - 2025 =",80)
print("Chúc mừng 80 năm ngày Quốc Khánh Việt Nam!")

#2
character_name = "Hi White"
character_age = "18"
print(f"anh trai tên là {character_name}")
print(f"anh trai {character_age} tuổi")
character_name = "parents"
character_age = "55"
print(f"gia đình tên là {character_name}")
print(f"gia đình {character_age} tuổi")

#3
diem = float(input("Nhập điểm lần 1 của bạn: "))
if diem >=5:
    diem_moi = diem + 2
else:
    diem_moi = diem + 5
diem_chinh = round(min(diem_moi, 10), 1)
print("Điểm lần 2 của bạn là:", diem_chinh)
