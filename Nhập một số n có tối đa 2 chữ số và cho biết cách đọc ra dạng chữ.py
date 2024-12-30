def dhdv(a,b=False):
    match a:
        case 1:
            return "mốt" if b else "một"
        case 2:
            return "hai"
        case 3:
            return "ba"
        case 4:
            return "bốn"
        case 5:
            return "lăm" if b else "năm"
        case 6:
            return "sáu"
        case 7:
            return "bảy"
        case 8:
            return "tám"
        case 9:
            return "chín"
        case 0:
            return " " if b else "không"

def dhc(b,c):
    match b:
        case 1:
            if c == 1:
                return "mười một"
            return "mười" + (" " + dhdv(c, b=True) if c!= 0 else "")
        case 2:
            return "hai mươi" + " " + (dhdv(c,b=True) if c!=0 else "")
        case 3:
            return "ba mươi" + " " + (dhdv(c, b=True) if c != 0 else "")
        case 4:
            return "bốn mươi" + " " + (dhdv(c, b=True) if c != 0 else "")
        case 5:
            return "năm mươi" + " " + (dhdv(c, b=True) if c != 0 else "")
        case 6:
            return "sáu mươi" + " " + (dhdv(c, b=True) if c != 0 else "")
        case 7:
            return "bảy mươi" + " " + (dhdv(c, b=True) if c != 0 else "")
        case 8:
            return "tám mươi" + " " + (dhdv(c, b=True) if c != 0 else "")
        case 9:
            return "chín mươi" + " " + (dhdv(c, b=True) if c != 0 else "")
        case 0:
            return dhdv(c)

def doc(n):
    if n<0 and n>99:
        print("nhập ngu")
    elif n<10:
        return dhdv(n)
    else:
        b=n//10
        c=n%10
        return dhc(b,c)

n=int(input("nhập số có tối đa 2 chữ số: "))
print(doc(n))


