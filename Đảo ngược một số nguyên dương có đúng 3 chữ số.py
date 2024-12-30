a=int(input("Nhập số có 3 chữ số:"))
if 100<=a<=999:
    b=a//100 #xử lý hàng đơn vị
    c=((a//10)%10)*10 #xử lí hàng chục
    d=(a%10)*100 #xử lí hàng trăm
    x = d + c + b
    print(f"Số đảo ngược là: {x}")
else:
    print("Bạn nhập sai rồi")