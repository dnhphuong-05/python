def ROI(r,c):
    return (r-c)/c
def Investment(roi):
    match roi:
        case roi if roi >=0.75:
            return "Should invest"
        case _:
            return "Don't invest"
print("ROI calculator")
r=int(input("Enter Revenue:"))
c=int(input("Enter cost:"))
roi=ROI(r,c)
print("Tỉ Lệ ROI =",roi)
print("==>",Investment(roi))