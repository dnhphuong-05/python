import time

def hinh_1():  # Vẽ hình vuông rỗng
    lines = []
    for y in range(n):
        line = ""
        for x in range(n):
            if y == 0 or y == n-1 or x == 0 or x == n-1:  # Nếu ở viền của hình vuông
                line += "*  "
            else:  # Bên trong hình vuông là khoảng trống
                line += "   "
        lines.append(line)
    return lines

def hinh_2():  # Vẽ hình tam giác
    lines = []
    for y in range(n):
        line = ""
        for x in range(n):
            if x <= y:
                line += "*  "
            else:
                line += "   "
        lines.append(line)
    return lines

def hinh_3():  # Vẽ hình số 3
    lines = []
    for y in range(3, -4, -1):
        line = ""
        for x in range(-3, 4):
            if (x > 0 and y > 0) or (x < 0 and y < 0):
                line += "  "
            elif x <= 0 and y >= 0:
                if abs(x) >= y:
                    if x == -2 and y == 1:
                        line += "  "
                        continue
                    line += "* "
                else:
                    line += "  "
            elif x >= 0 and y <= 0:
                if x >= abs(y):
                    if x == 2 and y == -1:
                        line += "  "
                        continue
                    line += "* "
                else:
                    line += "  "
        lines.append(line)
    return lines

def print_all_hinh_delay():  # In ra hình với độ trễ
    h1 = hinh_1()
    h2 = hinh_2()
    h3 = hinh_3()

    for i in range(n):  # In theo từng dòng của hình vuông và tam giác
        print(f"{h1[i]:<30} {h2[i]:<30}")
        time.sleep(e)

    print("\n" * 2)  # Tạo khoảng trống giữa hai phần
    # In hình số 3 ở bên dưới
    for line in h3:
        print(line)
        time.sleep(e)

n = int(input("Nhập vào độ cao của hình vuông/ hình tam giác: "))

# Nhập vào độ trễ
e = int(input("Nhập số giây delay: "))

print_all_hinh_delay()