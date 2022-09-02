lst = [4.00, 4.50, 5.00, 2.00, 1.50]

a,b = map(int, input().split())

print("Total: R$ {0:.2f}".format(lst[a-1]*b))