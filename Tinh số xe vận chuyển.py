def so_xe_van_chuyen(tong_tan):
    if tong_tan <= 10:
        i = 1  # Nếu tổng tấn nhỏ hơn hoặc bằng 10, chỉ cần 1 xe
    else:
        i = (tong_tan + 9) // 10  # Làm tròn lên bằng cách chia và thêm 9
    return i

# Nhập tổng số tấn cần vận chuyển
a = int(input("Tổng số tấn vận chuyển là: "))

# Gọi hàm tính và in ra số xe cần thiết
so_xe = so_xe_van_chuyen(a)
print(f"Tổng số xe vận chuyển cần thiết là: {so_xe}")