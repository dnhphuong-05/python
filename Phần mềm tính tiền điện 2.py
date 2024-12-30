print("Laddered cost of living: 1")
print("Business electricity: 2")
print("Electricity production: 3")
n=input("Choose an option you want: ")

def cost_of_living(a,b,c):
    if b-a<=0:
        return "Invalid Value"
    elif b-a <= 50*c:
        return f"pay for laddered cost of living: {(b-a) * 1484}"
    elif b-a<=100*c:
        return f"pay for laddered cost of living: {(50*c * 1484) + ((b-a) - 50*c) * 1533}"
    elif b-a<=200*c:
        return f"pay for laddered cost of living: {(50*c*1484) + (50*c*1533) + ((b-a) - 100*c) * 1786}"
    elif b-a<=300*c:
        return f"pay for laddered cost of living: {(50*c*1484) + (50*c*1533) + (100*c*1786) + ((b-a) - 200*c) * 2242}"
    elif b-a<=400*c:
        return f"pay for laddered cost of living: {(50*c*1484) + (50*c*1533) + (100*c*1786) + (100*c*2242) + ((b-a) - 300*c) * 2503}"
    elif b-a<=0:
        return "Invalid Value"
    else:
        return f"pay for laddered cost of living: {(50*c*1484) + (50*c*1533) + (100*c*1786) + (100*c*2242) + (100*c*2503) +((b-a) - 400*c) * 2587}"

def business_price(a,b):
    if b-a<=0:
        return "Invalid value"
    else:
        return f"pay for business electricity: {(b - a) * 2320}"

def production_price(a,b):
    if b-a<=0:
        return "Invalid value"
    else:
        return f"pay for electricity production: {(b-a)*1518}"

a=float(input("Old kilowatt-hour number:"))
b=float(input("New kilowatt-hour number:"))
c=float(input("Number of households sharing the same electricity meter:"))

x=cost_of_living(a,b,c)
y=business_price(a,b)
z=production_price(a,b)

match n:
    case "1":
        print(x)
    case "2":
        print(y)
    case "3":
        print(z)