from Tinhleapyear import checkleapyear, strtobool
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