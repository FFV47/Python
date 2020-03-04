print("Digite as dimensões da parede abaixo")

alt = float(input("Altura: "))
larg = float(input("Largura: "))

print(f"Area da parede = {alt*larg:.2f} m²")
print(f"Tinta necessária = {(alt*larg)/2:.2f} L")
