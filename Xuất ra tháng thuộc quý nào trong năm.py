def month(m):
    try:
        if m<0 or m>12:#Kiểm tra tháng ko hợp lệ
            raise ValueError("Tháng không hợp lệ")
        match m:
            case 1|2|3:
                    print(f"{m} thuộc quý I")
            case 4|5|6:
                    print(f"{m} thuộc quý II")
            case 7|8|9:
                    print(f"{m} thuộc quý III")
            case 10|11|12:
                print(f"{m} thuộc quý IV")
    except ValueError as e: #In ra thông báo lỗi nếu có ngoại lệ
        print(e)
m=int(input("nhập m:"))
month(m)