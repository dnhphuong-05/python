import math
r=float(input("nhập bán kính đường tròn: "))
def tinh_chu_vi(r):
    cv=2*math.pi*r
    return cv
def tinh_dien_tich(r):
    dt=math.pi*r**2
    return dt
#in kết quả
print("chu vi hình tròn= ", round(tinh_chu_vi(r),2))
print("chu vi hình tròn= ", tinh_dien_tich(r))
