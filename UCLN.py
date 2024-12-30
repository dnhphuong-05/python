def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Nhập hai số từ người dùng
A = int(input("Nhập số A: "))
B = int(input("Nhập số B: "))

# Tính UCLN
ketqua = ucln(A, B)
print(f"Ước số chung lớn nhất của {A} và {B} là: {ketqua}")