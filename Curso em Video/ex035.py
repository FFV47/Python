from termcolor import colored

print(colored("-+-", "yellow") * 20)
print(colored("Analisador de Triangulos", "blue"))
print(colored("-+-", "yellow") * 20)

print("Digite o comprimento de três segmentos de reta a seguir\n")
a = float(input("Digite o segmento A: "))
b = float(input("Digite o segmento B: "))
c = float(input("Digite o segmento C: "))

if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b):
    print("Os segmentos podem formar um triangulo!!")
else:
    print("Os segmentos NÃO podem formar um triangulo.")
