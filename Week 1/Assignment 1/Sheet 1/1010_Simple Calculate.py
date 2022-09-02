a,b,c = map(str, input().split())
d,e,f = map(str, input().split())

x=int(b)*float(c)+int(e)*float(f)

print("VALOR A PAGAR: R$ {0:.2f}".format(x))