num = []
par = []
impar = []

while True:
    n = str(input("Digite um valor [Digite 'S' para sair]: "))
    if n in "sS":
        break
    n = int(n)
    num.append(n)

print("\033[34m-=\033[m" * 40)
print(f"A lista digitada foi: \033[31m{num}\033[m")
print("\033[34m-=\033[m" * 40)

for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f"A lista de pares é \033[35m{par}\033[m")
print("\033[34m-=\033[m" * 40)
print(f"A lista de imapres é \033[36m{impar}\033[m")
