name = input("Nhập tên của bạn: ")
age = int(input("Nhập tuổi năm trước của bạn: "))
while (name == ""):
    print("Không hợp lệ! Vui lòng nhập lại.")
    name = input("Nhập tên của bạn: ")
while (age < 0) or (age > 120):
    print("Không hợp lệ! Vui lòng nhập lại.")
    age = int(input("Nhập tuổi năm trước của bạn: "))
print(f"Chào bạn {name}, bạn đang {age + 1} tuổi năm nay!")