print("\033[34m+\033[m" * 60)
print("\033[32m Comparador de Numeros \033[m")
print("\033[34m=\033[m" * 60)

n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))

if n1 > n2:
    print(f"\nO primeiro valor {n1} é maior.")
elif n2 > n1:
    print(f"\nO segundo valor {n2} é maior.")
else:
    print("Os dois numeros são iguais.")
