ev=0
od=0
pos=0
neg=0

for i in range(0,5):
    a=int(input())
    if a>0:
        pos+=1
    elif a<0:
        neg+=1
    if a%2==0:
        ev+=1
    else:
        od+=1

print("{} valor(es) par(es)".format(ev))
print("{} valor(es) impar(es)".format(od))
print("{} valor(es) positivo(s)".format(pos))
print("{} valor(es) negativo(s)".format(neg))