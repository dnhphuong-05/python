def so_ngay(m):
    if m not in range(1, 13):
        print("ValueError")
        return #kết thúc hàm nêu tháng không hợp le


    if m in (1,3,5,7,8,10,12):
        print("31 ngay")
    elif m==2:
        y=int(input("nhap nam "))
        if y%4==0 and y%100!=0 or y%400==0:
            print("29 ngay")
        else:
            print("28 ngay")
    else:
        "30 ngay"


m=int(input("nhap thang: "))
so_ngay(m)