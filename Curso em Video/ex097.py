def escreva(msg):
    tam = len(msg) + 4
    print("\033[31m~\033[m" * tam)
    print(f"  \033[34m{msg}\033[m")
    print("\033[31m~\033[m" * tam)


escreva("Gustavo Guanabara")
escreva("Curso em Video em Python")
escreva("CeV")
print()
