a = float(input())

if 0.00<=a<=400.00:
    print("Novo salario: {0:.2f}".format(a+(a*15)/100))
    print("Reajuste ganho: {0:.2f}".format((a*15)/100))
    print("Em percentual: 15 %")
elif 400.01<=a<=800.00:
    print("Novo salario: {0:.2f}".format(a+(a*12)/100))
    print("Reajuste ganho: {0:.2f}".format((a*12)/100))
    print("Em percentual: 12 %")
elif 800.01<=a<=1200.00:
    print("Novo salario: {0:.2f}".format(a+(a*10)/100))
    print("Reajuste ganho: {0:.2f}".format((a*10)/100))
    print("Em percentual: 10 %")
elif 1200.01<=a<=2000.00:
    print("Novo salario: {0:.2f}".format(a+(a*7)/100))
    print("Reajuste ganho: {0:.2f}".format((a*7)/100))
    print("Em percentual: 7 %")
else:
    print("Novo salario: {0:.2f}".format(a+(a*4)/100))
    print("Reajuste ganho: {0:.2f}".format((a*4)/100))
    print("Em percentual: 4 %")