a,b,c = map(int, input().split())

list = [a,b,c]
list.sort()

for i in list:
    print(i)
print("\n{}\n{}\n{}".format(a,b,c))