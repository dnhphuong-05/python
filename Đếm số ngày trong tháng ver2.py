def so_ngay(m,y):
    match m:
        case 1|3|5|7|8|10|12:
            return 31
        case 4|6|9|11:
            return 30
        case 2:
            if (y%4==0 and y%100!=0) or (y%400==0):
                return 29
            else:
                return 28
        case _:
            return "nhap ngu vai lon"
m = int(input("Nhập tháng:"))
y = int(input("Nhập năm:"))
ngay=so_ngay(m,y)
print(f"Tháng {m} có {ngay} ngay vào năm {y}")