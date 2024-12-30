def tinh_thue_nam(a):
    if 0 <= a <= 60:
        return a * 0.05
    elif 60 < a <= 120:
        return a * 0.1
    elif 120 < a <= 216:
        return a * 0.15
    elif 216 < a <= 384:
        return a * 0.2
    elif 384 < a <= 624:
        return a * 0.25
    elif 624 < a <= 960:
        return a * 0.3
    elif a > 960:
        return a * 0.35
    else:
        return "Invalid Value"

def tinh_thue_thang(b):
    if 0 <= b <= 5:
        return b * 0.05
    elif 5 < b <= 10:
        return b * 0.1
    elif 10 < b <= 18:
        return b * 0.15
    elif 18 < b <= 32:
        return b * 0.2
    elif 32 < b <= 52:
        return b * 0.25
    elif 52 < b <= 80:
        return b * 0.3
    elif b > 80:
        return b * 0.35
    else:
        return "Invalid Value"

# Nhập giá trị từ người dùng
a = float(input("Nhập phần thu nhập năm: "))
b = float(input("Nhập phần thu nhập tháng: "))

# Gọi hàm và lưu kết quả
x = tinh_thue_nam(a)
y = tinh_thue_thang(b)

# In kết quả ra màn hình
print(f"Thuế thu nhập cá nhân tính theo năm: {x}")
print(f"Thuế thu nhập cá nhân tính theo tháng: {y}")