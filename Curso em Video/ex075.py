tupla = ()

for c in range(4):
    tupla += (int(input("Digite um valor: ")),)

print(f"Você digitou os numeros {tupla}")
print(f"O numero 9 apareceu {tupla.count(9)} vezes.")
print(
    f"O valor 3 foi digitado primeiro na {tupla.index(3) + 1}ª posição."
    if 3 in tupla
    else "O valor 3 nao foi digitado."
)

print("Os numeros pares foram:", end=" ")
for i in tupla:
    if i % 2 == 0:
        print(i, end=" ")
print("\n")
