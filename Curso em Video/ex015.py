print("Digite abaixo as informações do carro alugado\n")

km = float(input("Digite os Km percorridos: "))
dia = int(input("Digite por quantos dias ele ficou alugado: "))

print(f"O cliente deverá pagar R$ {60 * dia + 0.15 * km:.2f}")
