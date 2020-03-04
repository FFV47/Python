tam = int(input("Digite uma tamanho para a matriz: "))
matriz = [[] for i in range(tam)]
par = 0
terceira = 0

print("-=" * 40)
for lin in range(tam):
    for col in range(tam):
        n = int(input(f"Digite um valor para a posição [{lin}, {col}]: "))
        matriz[lin].append(n)
        if n % 2 == 0:
            par += n
        if col == 2:
            terceira += n

print("-=" * 40)

for lin in matriz:
    for col in lin:
        print(f"[{col:^5}]", end="")
    print()

print("=-" * 40)
print(f"A soma dos valores pares da matriz é '{par}'")
print(f"A soma dos valores da terceira colula é '{terceira}'")
print(f"O maio valor da segunda linha é '{max(matriz[1])}'")
