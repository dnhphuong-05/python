def tinh_tien_dien_match_case(kwh_su_dung):
    # Tính tiền điện theo bậc với match-case
    match kwh_su_dung:
        case kwh if kwh <= 50:
            tong_tien = kwh * 1549
        case kwh if kwh <= 100:
            tong_tien = 50 * 1549 + (kwh - 50) * 1600
        case kwh if kwh <= 200:
            tong_tien = 50 * 1549 + 50 * 1600 + (kwh - 100) * 1858
        case kwh if kwh <= 300:
            tong_tien = 50 * 1549 + 50 * 1600 + 100 * 1858 + (kwh - 200) * 2340
        case kwh if kwh <= 400:
            tong_tien = 50 * 1549 + 50 * 1600 + 100 * 1858 + 100 * 2340 + (kwh - 300) * 2615
        case _:
            tong_tien = 50 * 1549 + 50 * 1600 + 100 * 1858 + 100 * 2340 + 100 * 2615 + (kwh_su_dung - 400) * 2701

    return tong_tien


# Hàm chính để yêu cầu thông tin từ người dùng
def chuong_trinh_tinh_tien_dien_match_case():
    ten_khach_hang = input("Nhập tên khách hàng: ")
    loai_khach_hang = input("Nhập loại khách hàng (sinh hoạt/ trả trước): ").lower()
    kwh_su_dung = float(input("Nhập số kWh đã sử dụng: "))

    match loai_khach_hang:
        case "sinh hoạt":
            tong_tien = tinh_tien_dien_match_case(kwh_su_dung)
        case "trả trước":
            tong_tien = kwh_su_dung * 2271
        case _:
            print("Loại khách hàng không hợp lệ!")
            return

    print(f"\nKhách hàng: {ten_khach_hang}")
    print(f"Số kWh đã sử dụng: {kwh_su_dung}")
    print(f"Tổng tiền điện phải trả: {tong_tien} VND")


# Gọi chương trình chính
chuong_trinh_tinh_tien_dien_match_case()
