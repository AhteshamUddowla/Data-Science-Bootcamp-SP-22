a = float(input())

if a>=0.00 and a<=2000.00:
    print("Isento")
elif a>=2000.01 and a<=3000.00:
    a=a-2000
    tax=a*.08
    print("R$ {0:.2f}".format(tax))
elif a>=3000.01 and a<=4500.00:
    a=a-3000
    tax=a*.18+80
    print("R$ {0:.2f}".format(tax))
else:
    a=a-4500
    tax=a*.28+350
    print("R$ {0:.2f}".format(tax))