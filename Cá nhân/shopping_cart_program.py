foods = []
prices = []
total = 0
while True:
    food = input("Nhập tên món ăn (Khi muốn dừng lại thì nhập 'E'): ")
    if food == "" or food.lower() == "e":
        break
    else:
        price = int(input("Nhập giá món ăn: "))
        foods.append(food)
        prices.append(price)
print("-----Hoá Đơn-----")
for x in foods:
    print(x, end = "; ")
for y in prices:
    total += y
print(f"\nTổng cộng các món: {total} VND.")