from math import sqrt

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))


def phuong_trình_bậc2():
    if a==0:
        def phuong_trinh_bac1():
            if b == 0:
                if c == 0:
                    print("phương trình vô số nghiệm")
                else:
                    print("phương trình vô nghiệm")
            else:
                x = -c / b
                print(f"phương trình có nghiệm x = ", {x})
        return phuong_trinh_bac1()
    else:
        delta=b**2-4*a*c
        if delta>0:
            x1=(-b-sqrt(delta))/(2*a)
            x2=(-b + sqrt(delta)) / (2 * a)
            print(f"phương trình có 2 nghiệm x1={x1} và x2={x2}")
        elif delta==0:
            print(f"phương trình có nghiệm kép là", -b/2*a)
        else:
            print("phuong trình vô nghiệm")

phuong_trình_bậc2()
