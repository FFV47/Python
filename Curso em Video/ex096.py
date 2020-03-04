def titulo(msg):
    print("\033[31m-\033[m" * 60)
    print(f"\033[34m{msg:^60}\033[m")
    print("\033[31m-\033[m" * 60)


def area(l, w):
    print(f"Área do terreno de {l:.2f}x{w:.2f} é de {l*w:.2f} m²")


titulo("Area do Terreno")

largura = float(input("Largura do Terreno [m]: "))
comp = float(input("Comprimento do Terreno [m]: "))
area(largura, comp)
print()
