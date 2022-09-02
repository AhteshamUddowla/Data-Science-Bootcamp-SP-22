su=0
pos=0

for i in range(0,6):
    a=float(input())
    if a>0:
        pos+=1
        su+=a
  
print("{} valores positivos".format(pos))
print("{0:.1f}".format(su/pos))
