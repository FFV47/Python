from random import shuffle

print("Digite o nome dos 4 alunos abaixo\n")

al1 = input("Primeiro aluno: ")
al2 = input("Segundo aluno: ")
al3 = input("Terceiro aluno: ")
al4 = input("Quarto aluno: ")

lista = [al1, al2, al3, al4]

shuffle(lista)
print(f"\nA ordem de apresentação será: {lista}")

print("\nA ordem de apresentação será")
for i in range(4):
    print(f"{i+1}º aluno(a):", lista[i])
