print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Fibonacci em While':^60} \033[m")
print("\033[34m=\033[m" * 60)

num = int(input("Digite o numero de elementos de fibonacci: "))

i = 1
fibo_depois = 0
fibo_soma = 0

print("Sequência de Fibonacci:", end=" ")
while i <= num:
    if i == 2:
        fibo_antes = 0
        fibo_depois = 1
    fibo_antes = fibo_depois
    fibo_depois = fibo_soma
    fibo_soma = fibo_depois + fibo_antes
    print(
        f"\033[1;31m{fibo_soma}\033[m > " if i != num else f"\033[31m{fibo_soma}\033[m",
        end="",
    )
    i += 1
