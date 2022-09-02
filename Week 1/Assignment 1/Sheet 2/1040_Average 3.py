a,b,c,d = map(float, input().split())

s=a*2+b*3+c*4+d
avg = s/10

print("Media: {0:.1f}".format(avg))

if avg >= 7.0:
    print("Aluno aprovado.")
elif avg<5.0:
    print("Aluno reprovado.")
elif 5.0<=avg<=6.9:
    print("Aluno em exame.")
    e = float(input())
    print("Nota do exame: {0:.1f}".format(e))
    avg=(avg+e)/2
    if avg>=5.0:
        print("Aluno aprovado.")
    elif avg <= 4.9:
        print("Aluno reprovado.")
    print("Media final: {0:.1f}".format(avg))