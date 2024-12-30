t=int(input("Nhập số giây:"))
def thoigian(t):
    h = (t// 3600) % 24
    m = (t % 3600) // 60
    s = (t % 3600) % 60
    return print(f"{h}:{m}:{s}",["AM","PM"][h>12])
thoigian(t)
"""h > 12 là một biểu thức so sánh, kết quả sẽ là True nếu h lớn hơn 12 (chiều) và False nếu h nhỏ hơn hoặc bằng 12 (sáng).
Python coi False là 0 và True là 1 khi sử dụng trong chỉ số của danh sách, vì vậy:
Nếu h <= 12, thì h > 12 là False, tương đương với 0, do đó ["AM", "PM"][0] trả về "AM".
Nếu h > 12, thì h > 12 là True, tương đương với 1, do đó ["AM", "PM"][1] trả về "PM"."""