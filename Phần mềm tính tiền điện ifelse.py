def tinh_tien_dien_if_else(kwh_su_dung):
    # Tính tiền điện theo bậc với if-else
    if kwh_su_dung <= 50:
        tong_tien = kwh_su_dung * 1549
    elif kwh_su_dung <= 100:
        tong_tien = 50 * 1549 + (kwh_su_dung - 50) * 1600
    elif kwh_su_dung <= 200:
        tong_tien = 50 * 1549 + 50 * 1600 + (kwh_su_dung - 100) * 1858
    elif kwh_su_dung <= 300:
        tong_tien = 50 * 1549 + 50 * 1600 + 100 * 1858 + (kwh_su_dung - 200) * 2340
    elif kwh_su_dung <= 400:
        tong_tien = 50 * 1549 + 50 * 1600 + 100 * 1858 + 100 * 2340 + (kwh_su_dung - 300) * 2615
    else:
        tong_tien = 50 * 1549 + 50 * 1600 + 100 * 1858 + 100 * 2340 + 100 * 2615 + (kwh_su_dung - 400) * 2701

    return tong_tien


# Hàm chính để yêu cầu thông tin từ người dùng
def chuong_trinh_tinh_tien_dien_if_else():
    ten_khach_hang = input("Nhập tên khách hàng: ")
    loai_khach_hang = input("Nhập loại khách hàng (sinh hoạt/ trả trước): ").lower()
    kwh_su_dung = float(input("Nhập số kWh đã sử dụng: "))

    if loai_khach_hang == "sinh hoạt":
        tong_tien = tinh_tien_dien_if_else(kwh_su_dung)
    elif loai_khach_hang == "trả trước":
        tong_tien = kwh_su_dung * 2271
    else:
        print("Loại khách hàng không hợp lệ!")
        return

    print(f"\nKhách hàng: {ten_khach_hang}")
    print(f"Số kWh đã sử dụng: {kwh_su_dung}")
    print(f"Tổng tiền điện phải trả: {tong_tien} VND")


# Gọi chương trình chính
chuong_trinh_tinh_tien_dien_if_else()
