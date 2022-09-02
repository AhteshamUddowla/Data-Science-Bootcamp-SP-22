n = int(input())

iin=0
out=0

for i in range(0,n):
   a = int(input())
   if 10<=a<=20:
       iin+=1
   else:
       out+=1
print("{} in\n{} out".format(iin,out))