def tinh_thue_tncns(thunhap):
    # Giảm trừ gia cảnh
    giam_tru = 11_000_000  # Giảm trừ cho bản thân
    thunhap_chiu_thue = thunhap - giam_tru

    if thunhap_chiu_thue <= 0:
        return 0

    thue = 0

    # Tính thuế theo từng bậc
    if thunhap_chiu_thue <= 60_000_000:
        thue = 0
    elif thunhap_chiu_thue <= 120_000_000:
        thue = (thunhap_chiu_thue - 60_000_000) * 0.05
    elif thunhap_chiu_thue <= 216_000_000:
        thue = (60_000_000 * 0.05) + (thunhap_chiu_thue - 120_000_000) * 0.10
    elif thunhap_chiu_thue <= 384_000_000:
        thue = (60_000_000 * 0.05) + (96_000_000 * 0.10) + (thunhap_chiu_thue - 216_000_000) * 0.15
    elif thunhap_chiu_thue <= 624_000_000:
        thue = (60_000_000 * 0.05) + (96_000_000 * 0.10) + (168_000_000 * 0.15) + (thunhap_chiu_thue - 384_000_000) * 0.20
    elif thunhap_chiu_thue <= 960_000_000:
        thue = (60_000_000 * 0.05) + (96_000_000 * 0.10) + (168_000_000 * 0.15) + (240_000_000 * 0.20) + (thunhap_chiu_thue - 624_000_000) * 0.25
    elif thunhap_chiu_thue <= 1_200_000_000:
        thue = (60_000_000 * 0.05) + (96_000_000 * 0.10) + (168_000_000 * 0.15) + (240_000_000 * 0.20) + (336_000_000 * 0.25) + (thunhap_chiu_thue - 960_000_000) * 0.30
    else:
        thue = (60_000_000 * 0.05) + (96_000_000 * 0.10) + (168_000_000 * 0.15) + (240_000_000 * 0.20) + (336_000_000 * 0.25) + (240_000_000 * 0.30) + (thunhap_chiu_thue - 1_200_000_000) * 0.35

    return thue

# Nhập thu nhập
thunhap = float(input("Nhập thu nhập hàng tháng: "))
thue = tinh_thue_tncns(thunhap)
print(f"Thuế thu nhập cá nhân cần nộp: {thue:,.0f} VND")
