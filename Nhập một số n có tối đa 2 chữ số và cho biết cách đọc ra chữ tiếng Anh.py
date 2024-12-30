def hdv(a):
    match a:
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case 5:
            return "five"
        case 6:
            return "six"
        case 7:
            return "seven"
        case 8:
            return "eight"
        case 9:
            return "nine"
        case 0:
            return "zero"
def hc(b,c):
    match b:
        case 1:
            if c==0:
                return "ten"
            if c==1:
                return "eleven"
            elif c==2:
                return "twelve"
            elif c==3:
                return "thirteen"
            elif c==5:
                return "fifteen"
            return hdv(c)+"teen"
        case 2:
            if c==0:
                return "twenty"
            return "twenty"+("-"+hdv(c))
        case 3:
            if c == 0:
                return "thirty"
            return "thirty" + ("-" + hdv(c))
        case 4:
            if c == 0:
                return "fourty"
            return "fourty" + ("-" + hdv(c))
        case 5:
            if c == 0:
                return "fifty"
            return "fifty" + ("-" + hdv(c))
        case 6:
            if c == 0:
                return "sixty"
            return "sixty" + ("-" + hdv(c))
        case 7:
            if c == 0:
                return "seventy"
            return "seventy" + ("-" + hdv(c))
        case 8:
            if c == 0:
                return "eightty"
            return "eightty" + ("-" + hdv(c))
        case 9:
            if c == 0:
                return "ninety"
            return "ninety" + ("-" + hdv(c))
        case 0:
            return hdv(c)

def doc(n):
    if n<0 and n>99:
        print ("nhập ngu")
    elif n<10:
        return hdv(n)
    else:
        b=n//10
        c=n%10
        return hc(b,c)
n=int(input("nhập 2 số: "))
print(doc(n))