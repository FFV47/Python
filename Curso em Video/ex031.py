viagem = float(input("Digite a distancia da viagem em Km: "))

if viagem <= 200:
    print(f"Viagem abaixo de 200 Km -> Preço da passagem: R$ {viagem * 0.5 :.2f}")
else:
    print(f"Viagem acima de 200 Km -> Preço da passagem: R$ {viagem * 0.45 :.2f}")

preco = viagem * 0.5 if viagem <= 200 else viagem * 0.45

print(f"\nPreço da passagem: R$ {preco:.2f}")
