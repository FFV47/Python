print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Palindromo':^60} \033[m")
print("\033[34m=\033[m" * 60)

frase = str(input("Digite uma frase: ")).strip().upper()

frase2 = frase.replace(" ", "")

invertida = ""

# Primeira Solução
for i in range(len(frase2) - 1, -1, -1):
    invertida += frase2[i]

# Segunda Solução
invertida = frase2[::-1]

print(f"A frase \033[33m{frase2}\033[m invertida é: \033[35m{invertida}\033[m")

if frase2 == invertida:
    print(f"\nA frase: '\033[32m{frase}\033[m', é um palindromo")
else:
    print(f"\nA frase '\033[32m{frase}\033[m', não é um palindromo")
