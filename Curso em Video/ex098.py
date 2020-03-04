from time import sleep


def contagem(ini, fim, step):
    if step == 0:
        step = 1
    step = abs(step)
    print("-=" * 20)
    if fim > ini:
        print(f"Contagem de {ini} até {fim} de {step} em {step}")
        for i in range(ini, fim + 1, step):
            print(f"{i}", end=" ")
            sleep(0.3)
        print("FIM!")
    else:
        print(f"Contagem de {ini} até {fim} de {step} em {step}")
        step = -step
        for i in range(ini, fim - 1, step):
            print(f"{i}", end=" ")
            sleep(0.3)
        print("FIM!")


contagem(1, 10, 1)
contagem(10, 0, 2)
print("-=" * 20)
print("Agora é a sua vez de personalizar a contagem!")
ini = int(input(f"{'Início: ':<8}"))
fim = int(input(f"{'Fim: ':<8}"))
step = int(input(f"{'Passo: ':<8}"))
print("-=" * 20)
contagem(ini, fim, step)
print()
