from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
argv.append(str(input("Type your name: ")))
argv.append(int(input("Type your age: ")))
print(argv)

# 'argv' cria uma lista com todos os argumentos passados para o interpretador. Pode-se desempacotar a lista colocando as variáveis separadas por virgulas.
