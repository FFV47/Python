def fatorial(num, show=False):
    """Calcula o fatorial de um Numero

    Args:
        num (int): Numero a ser calculado
        show (bool, optional): Mostra ou não o processo. Defaults to False.

    Returns:
        int: Retorna o fatorial do numero pedido
    """
    print("-" * (num * 5))
    fat = 1
    if num == 0:
        return 1
    for i in range(num, 0, -1):
        if show is False:
            fat *= i
        else:
            fat *= i
            print(f"{i} x" if i != 1 else f"{i} =", end=" ")
    return fat


n = int(input("Numero: "))
while True:
    resp = str(input("Deseja mostrar os calculos [S/N]? "))
    if resp in "Ss":
        s = True
        break
    elif resp in "Nn":
        s = False
        break
    else:
        print("Resposta inválida. Tente novamente.")
print(fatorial(n, s))
