import math

a,b,c = map(float, input().split())

s=b*b-4*a*c

if s<0 or a==0:
    print("Impossivel calcular")
else:
    r1=(-b+math.sqrt(s))/(2*a)
    print("R1 = {0:.5f}".format(r1))
    r2=(-b-math.sqrt(s))/(2*a)
    print("R2 = {0:.5f}".format(r2))
    
