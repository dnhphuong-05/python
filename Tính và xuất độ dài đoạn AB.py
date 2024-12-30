import math
def length(a,b,c,d):
    length=math.sqrt((c-a)**2+(d-b)**2)
    return print("Độ dài đoạn thẳng AB là:",abs(round(length,2)))
a=float(input("Nhập Xa:"))
b=float(input("Nhập Ya:"))
c=float(input("Nhập Xb:"))
d=float(input("Nhập Yd:"))
length(a,b,c,d)