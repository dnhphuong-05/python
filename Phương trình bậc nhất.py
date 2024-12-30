a=float(input("a = "))
b=float(input("b = "))

def phuong_trinh_bac1():
    if a==0:
        if b==0:
            print("phương trình vô số nghiệm")
        else:
            print("phương trình vô nghiệm")
    else:
        x=-b/a
        print(f"phương trình có nghiệm x = ",{x})

phuong_trinh_bac1()

