x=str(input("Customer name: "))
a=int(input("Number of kWh used: "))
b=int(input("Customer group: "))
def sodien(a):
    if b==1:
        if 0<a<=50:
            return 1549*a
        elif a<=100:
            return 1600*a
        elif a<=200:
            return 1858*a
        elif a<=300:
            return 2340*a
        elif a<=400:
            return 2615*a
        elif a>400:
            return 2701*a
        else:
            return "Invalid value"
    elif b==2:
        if a>0:
            return 2271*a
        else:
            return "Invalid value"
    else:
        print ("Invalid value")
c=sodien(a)
print(f"The amount to be paid: {c}")