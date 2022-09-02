n = int(input())
m = int(input())
neg=0

if(n>m):
    for i in range(m+1,n):
        if i%2==1:
            neg+=i
    print(neg)
else:
    for i in range(n+1,m):
        if i%2==1:
            neg+=i
    print(neg)