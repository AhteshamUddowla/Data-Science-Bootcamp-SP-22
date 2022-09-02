a,b,c = map(float, input().split())

x=.5*a*c
print("TRIANGULO: {0:.3f}".format(x))

x=3.14159*c*c
print("CIRCULO: {0:.3f}".format(x))

x=.5*(a+b)*c
print("TRAPEZIO: {0:.3f}".format(x))

x=b*b
print("QUADRADO: {0:.3f}".format(x))

x=a*b
print("RETANGULO: {0:.3f}".format(x))