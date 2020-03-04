def leiaInt(msg):
    while True:
        num = str(input(msg)).strip()
        if num.isnumeric() is True:
            return int(num)
        print("ERRO!!! Numero inteiro inválido")


# Solução ruim
# def leiaInt(msg):
#     while True:
#         num = str(input(msg)).strip()
#         i = 0
#         for i, v in enumerate(num):
#             if v not in "0123456789":
#                 i = -1
#                 break
#         if i == len(num) - 1:
#             return int(num)
#         else:
#             print("ERRO! numero inteiro inválido")


# Main
n = leiaInt("Digite um numero: ")
print(f"Você acabou de digitar o numero {n}")
