from math import sqrt
def dt_tam_giac(a,b,c):
    try:
        if  (a<=0 or b <=0 or c <=0) or (a+b)<=c or (a+c)<=b or b+c<=a:
            print("tam giác không hợp lệ")
        else:
            cv = a + b + c
            p = cv / 2
            dt = sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"diện tích tam giác là: {dt}")
    except ValueError:
        print("giá tri nhập vào khong hợp lệ")
a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
c=float(input("Nhập c:"))
kqua=dt_tam_giac(a,b,c)
print(kqua)