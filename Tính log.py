import math
a=float(input("a:"))
x=float(input("x:"))
print (["Ngu như bò"," "][a>0])
print (["Ngu như bò"," "][x>0])
print (["Ngu như bò"," "][a!=1])
log=math.log10(x)/math.log10(a)
print("log",log)