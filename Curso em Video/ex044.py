print("\033[34m+\033[m" * 60)
print(f"\033[32m{' Calculo de Preço ':^60}\033[m")
print("\033[34m=\033[m" * 60)

produto = float(input("Digite o preço do produto: "))
condiçao = str(input("Digite a condição de pagamento: "))
vezes = int(input("Digite em quantas vezes você deseja dividir: "))

if condiçao == "dinheiro" or condiçao == "cheque" and vezes == 1:
    print(
        f"Você ganhou 10% de desconto, de R$ {produto:.2f} por R$ {produto * 0.9:.2f}"
    )
elif condiçao == "cartao" and vezes == 1:
    print(
        f"Você ganhou 5% de desconto, de R$ {produto:.2f} por R$ {produto * 0.95:.2f}"
    )
elif condiçao == "cartao" and vezes == 2:
    print(f"Nessa condição nao existe desconto:")
    print(f"Preço: R$ {produto:.2f}")
    print(f"Prestação: R$ {produto / vezes}")
elif condiçao == "cartao" and vezes >= 3:
    print(f"Essa condição tem 20% de juros:")
    print(f"Preço: R$ {produto * 1.2:.2f}")
    print(f"Prestação: R$ {produto * 1.2 / vezes:.2f}")
else:
    print("Você não preencheu o formulario corretamente.")
