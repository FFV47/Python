from time import sleep


def titulo(msg):
    tam = len(msg) + 4
    print("\033[37;44m~\033[m" * tam)
    print(f"\033[37;44m  {msg}  \033[m")
    print("\033[37;44m~\033[m" * tam)


def mensagem(msg):
    tam = len(msg) + 4
    print("\033[37;42m~\033[m" * tam)
    print(f"\033[37;42m  {msg}  \033[m")
    print("\033[37;42m~\033[m" * tam)


def pyhelp(lib):
    help(help)


# MAIN
while True:
    titulo("SISTEMA DE AJUDA PyHELP")
    lib = str(input("\033[37;41mFunção ou Biblioteca > "))
    if lib.upper() == "FIM":
        mensagem("FINALIZANDO")
        sleep(1)
        break
    mensagem(f"Acessando o manual do comando '{lib}'")
    sleep(2)
    help(lib.__doc__)

print()
