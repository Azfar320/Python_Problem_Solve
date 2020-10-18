#Average 3

N1,N2,N3,N4 = input().split()

n1 = float(N1)
n2 = float(N2)
n3 = float(N3)
n4 = float(N4)

Average1 = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/(2+3+4+1)


print("Media: %.1f"%Average1)

if Average1>=7.0:
    print("Aluno aprovado.")
elif Average1<5.0:
    print("Aluno reprovado.")
elif Average1>=5.0 and Average1<7.0:
    print("Aluno em exame.")
    a = input("")
    a1 = float(a)
    print("Nota do exame: %.1f"%a1)
    Average2 = (Average1+a1)/2
    if Average2>=5.0:
        print("Aluno aprovado.")
    elif Average2<=4.9:
        print("Aluno reprovado.")
    print("Media final: %.1f"%Average2)