lista = [[] for k in range(2)]

for c in range(7):
    n = int(input(f"Digite o {c+1}º valor: "))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)


lista[0].sort()
lista[1].sort()
print("-" * 60)
print(f"Os valores pares digitados foram:", lista[0])
print("-" * 60)
print(f"Os valores impares digitados foram:", lista[1])
print()
