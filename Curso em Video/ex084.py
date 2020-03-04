lista = []
dados = []
maior = menor = 0

while True:
    dados.append(str(input("Digite seu nome: ")))
    dados.append(float(input("Digite seu peso: ")))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()

    n = str(input("Deseja continuar? [S/N] "))
    if n in "nN":
        break

print("\033[32m=-\033[m" * 40)
print(f"Você cadastrou {len(lista)} pessoas")
print("\033[32m=-\033[m" * 40)

print(f"O maior peso foi {maior:.2f} Kg, que é o peso de", end=" ")
for p in lista:
    if p[1] == maior:
        print(f"'\033[34m{p[0]}\033[m'", end=" ")
print()

print(f"O menor peso foi {menor:.2f} Kg, que é o peso de", end=" ")
for p in lista:
    if p[1] == menor:
        print(f"'\033[34m{p[0]}\033[m'", end=" ")

print()
