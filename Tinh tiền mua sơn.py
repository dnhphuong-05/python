a = int(input("Nhập số thùng sơn mua: "))


def tinh_tien_mua_son():
    # Tính tổng tiền
    tong_tien = a * 350000
    print(f"Số tiền mua sơn là: {tong_tien} VND")

    # Tính số nón được tặng
    so_non = a // 3
    # Tính số thùng dư để tặng bút
    so_but = (a%3) * 2

    # In kết quả
    print(f"Số nón được tặng: {so_non}")
    print(f"Số bút được tặng: {so_but}")


# Gọi hàm để tính toán
tinh_tien_mua_son()