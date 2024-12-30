def tinh_dtb(a,b,c):
    dtb= (a+b+c)/3
    return dtb

a=float(input("nhập điểm toán: "))
b=float(input("nhập điểm lý: "))
c=float(input(":nhập điểm hoá: "))

print("điểm trung bình là: ", round(tinh_dtb(a,b,c), 2))