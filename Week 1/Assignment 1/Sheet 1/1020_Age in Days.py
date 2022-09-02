n = int(input())

y = n//365
n %= 365
m = n//30
n %= 30
d = n
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(y,m,d))
