nome = input("Digite o nome de uma cidade: ").strip().upper()

print("O nome da cidade começa com Santo?", "SANTO" in nome.split()[0])

print("O nome da cidade começa com Santo?", nome[:5] == "SANTO")
