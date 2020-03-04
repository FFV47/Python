def ficha(jog, gols):

    if jog == "":
        jog = "<desconhecido>"
    if gols == "":
        gols = 0
    print(f"O jogador {jog} fez {gols} gol(s) no campeonato.")


# Main
nome = str(input("Nome do jogador: "))
gols = str(input("Gols marcados: "))
ficha(nome, gols)
