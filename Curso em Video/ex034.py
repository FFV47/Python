sal = float(input("Digite o salário do funcionário: "))

if sal >= 1250:
    print(
        f"\nSalário com aumento de 10%:\nAtual: R$ {sal:.2f} Futuro: R$ {sal * 1.1 :.2f}"
    )
else:
    print(
        f"\nSalário com aumento de 15%:\nAtual: R$ {sal:.2f} Futuro: R$ {sal * 1.15 :.2f}"
    )
