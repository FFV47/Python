print("\033[31mTESTE")  # vermelho
print("\033[1;33mTESTE")  # bold; amarelo
print("\033[1;32;43mTESTE\033[m")  # fundo amarelo
print("\033[;30mTESTE")  # preto
print("\033[;37mTESTE")  # branco
print("\n\033[7mTESTE\033[m")  # invertido


nome = "fernando"

print(f"Muito prazer em te conhecer \033[1;31;42m{nome}\033[m")
