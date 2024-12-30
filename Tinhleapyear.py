def checkleapyear(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False
def strtobool(s):
    return s.lower() in ("1","c","true",)

while True:
    year=int(input("Input year:"))
    result=checkleapyear(year)
    if result==True:
        print(year,'is a leap year')
    else:
        print(year,'is NOT a leap year')
    ask=input("Continue?(1/2):")
    r=strtobool(ask)
    if r==False:
        print("BYEEEEE!!!!!")
        break