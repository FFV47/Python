from math import trunc, ceil

num = float(input("Digite um numero real: "))

print(f"A parte inteira de {num:.3f} é: {trunc(num)}")
print(f"Arrendondamento pra cima {ceil(num)}")
