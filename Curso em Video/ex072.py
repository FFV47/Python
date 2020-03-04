tupla = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quartorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)

while True:
    opcao = int(input("Digite um número entre 0 e 20 [999 para terminar]: "))
    if opcao == 999:
        break

    while opcao not in range(21):
        opcao = int(input("Tente Novamente, Digite um número entre 0 e 20: "))
        if opcao == 999:
            break

    print(f"Voce digitou o número {tupla[opcao]}")