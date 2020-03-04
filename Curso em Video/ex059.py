from time import sleep

print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Menu em While':^60} \033[m")
print("\033[34m=\033[m" * 60)

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

opcao = -1

while opcao != 5:
    print("\n" + "\033[36m-=\033[m" * 20)
    print("[1] SOMAR")
    print("[2] MULTIPLICAR")
    print("[3] MAIOR")
    print("[4] NOVOS NUMEROS")
    print("[5] SAIR DO PROGRAMA")
    opcao = int(input("\nEscolha uma das opções acima: "))

    if opcao == 1:
        print(f"\033[32mSoma de {num1} + {num2} = {num1 + num2}\033[m")
    elif opcao == 2:
        print(f"\033[34mMultiplicaçao de {num1} x {num2} = {num1 * num2}\033[m")
    elif opcao == 3:
        if num1 > num2:
            print(f"\033[33mMaior: {num1}\033[m")
        else:
            print(f"\033[33mMaior: {num2}\033[m")
    elif opcao == 4:
        num1 = int(input("\n\033[36mDigite o primeiro valor:\033[m "))
        num2 = int(input("\033[36mDigite o segundo valor: \033[m"))
    elif opcao == 5:
        print("Finalizando...")
        sleep(2)
    else:
        print("\033[31mOpção inválida, tente novamente.\033[m")

print("\nFIM")
