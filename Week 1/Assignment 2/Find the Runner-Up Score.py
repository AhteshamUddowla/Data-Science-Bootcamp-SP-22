n = int(input())

lst = map(int, input().split())
lst = list(lst)

mx = max(lst)
mn = -101

for i in range(n):
    if lst[i]<mx and lst[i] > mn:
        mn = lst[i]

print(mn)