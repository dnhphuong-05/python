# Hàm kiểm tra năm nhuận
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Hàm tính ngày kế tiếp
def next_day(dd, mm, yyyy):
    # Số ngày trong từng tháng
    days_in_month = [31, 29 if is_leap_year(yyyy) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Kiểm tra tính hợp lệ của ngày nhập vào
    if dd < 1 or dd > days_in_month[mm - 1] or mm < 1 or mm > 12:
        return "Ngày không hợp lệ. Vui lòng nhập lại."

    # Kiểm tra ngày cuối tháng
    if dd < days_in_month[mm - 1]:
        dd += 1
    else:
        # Ngày đầu của tháng kế tiếp
        dd = 1
        if mm == 12:
            # Ngày đầu của năm kế tiếp
            mm = 1
            yyyy += 1
        else:
            mm += 1

    return f"{dd}/{mm}/{yyyy}"


# Nhập vào ngày, tháng, năm
dd = int(input("Nhập ngày: "))
mm = int(input("Nhập tháng: "))
yyyy = int(input("Nhập năm: "))
print(f"Ngày bạn cần kiểm tra là: {dd}/{mm}/{yyyy}")

# In ra ngày kế tiếp
print(f"Ngày tiếp theo là: {next_day(dd, mm, yyyy)}")
