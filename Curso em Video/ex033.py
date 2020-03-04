n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

# primeiro metodo

if n1 > n2 > n3:
    print(f"\nMaior: {n1}")
    print(f"Menor: {n3}")
if n1 > n3 > n2:
    print(f"\nMaior: {n1}")
    print(f"Menor: {n2}")
if n2 > n1 > n3:
    print(f"\nMaior: {n2}")
    print(f"Menor: {n3}")
if n2 > n3 > n1:
    print(f"\nMaior: {n2}")
    print(f"Menor: {n1}")
if n3 > n2 > n1:
    print(f"\nMaior: {n3}")
    print(f"Menor: {n1}")
if n3 > n1 > n2:
    print(f"\nMaior: {n3}")
    print(f"Menor: {n2}")

# segundo metodo

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f"\nMaior: {maior}")

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f"Menor: {menor}")
