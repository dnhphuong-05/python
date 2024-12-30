import time

def hinh_1_line(): #Vẽ hình 1
    lines = []
    for y in range(3, -4, -1):
        line = ""
        for x in range(-3, 4):
            if x > 0 > y or x < 0 < y:
                line += "  "
            elif x >= 0 and y >= 0:
                if x + y <= 3:
                    line += "* "
                else:
                    line += "  "
            elif x <= 0 and y <= 0:
                if x <= y:
                    line += "* "
                else:
                    line += "  "
        lines.append(line)
    return lines

def hinh_2_line(): #Vẽ hình 2
    lines = []
    for y in range(3, -4, -1):
        line = ""
        for x in range(-3, 4):
            if x > 0 > y or x < 0 < y:
                line += "  "
            elif x >= 0 and y >= 0:
                if x + y <= 3:
                    if x == y == 1:
                        line += "  "
                        continue
                    line += "* "
                else:
                    line += "  "
            elif x <= 0 and y <= 0:
                if x <= y:
                    if x == -2 and y == -1:
                        line += "  "
                        continue
                    line += "* "
                else:
                    line += "  "
        lines.append(line)
    return lines

def hinh_3_line(): #Vẽ hình 3
    lines = []
    for y in range(3, -4, -1):
        line = ""
        for x in range(-3, 4):
            if y > 0 > x:
                line += "  "
            elif x > 0 and y > 0:
                if x == y:
                    for z in range(x + 1):
                        line += "* "
            elif x <= 0 and y <= 0:
                if x == y:
                    for j in range(3 + y):
                        line += "  "
                    for z in range(-y + 1):
                        line += "* "
        lines.append(line)
    return lines

def hinh_4_line(): #Vẽ hình 4
    lines = []
    for y in range(3, -4, -1):
        line = ""
        for x in range(-3, 4):
            if y > 0 > x:
                line += "  "
            elif x > 0 and y > 0:
                if x == y:
                    for z in range(x + 1):
                        if x == 2 and y == 2 and z == 1:
                            line += '  '
                            continue
                        line += "* "
            elif x <= 0 and y <= 0:
                if x == y:
                    for j in range(3 + y):
                        line += "  "
                    for z in range(-y + 1):
                        if x == -2 and y == -2 and z == 1:
                            line += '  '
                            continue
                        line += "* "
        lines.append(line)
    return lines

def print_all_in_one_with_delay():
    h1 = hinh_1_line()
    h2 = hinh_2_line()
    h3 = hinh_3_line()
    h4 = hinh_4_line()

    for i in range(len(h1)):  # Các hình có cùng số dòng
        print(f"{h1[i]:<20} {h2[i]:<20} {h3[i]:<20} {h4[i]:<20}")
        time.sleep(n)  # Chờ n giây sau khi in mỗi dòng

#Nhập độ trễ
n=int(input("Nhập số giây delay:"))

#In ra
print_all_in_one_with_delay()