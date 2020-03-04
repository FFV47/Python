nome = input("Digite seu nome completo: ")

print("Nome em caixa alta:", nome.upper())

print("Nome com minusculas:", nome.lower())

print("Quantidade de letras:", len("".join(nome.split())))

print(f'Quantidade de letras: {len(nome.replace(" ",""))}')

print(f"Quantidade de letras: {len(nome) - nome.count(' ')}")

print("Tamanho da string:", len(nome))

print(f"Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras")
