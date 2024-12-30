def test_leap(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

def strtobool(s):
    return s.lower() in ("co", "c","1")

while True:
    year=int(input("nhap nam: "))
    result=test_leap(year)
    if result==True:
        print("day la nam nhuan")
    else:
        print("day khong phai nam nhuan")
    ask=input("continue(co/khong): ")
    r=strtobool(ask)
    if r==False:
        print("Byeee")
        break






