campeonato = (
    "Santos",
    "Palmeiras",
    "Flamengo",
    "Atlético Mineiro",
    "São Paulo",
    "Corinthians",
    "Botafogo",
    "Internacional",
    "Ceará",
    "Bahia",
    "Atlético-PR",
    "Fortaleza",
    "Goiás",
    "Grêmio",
    "Vasco da Gama",
    "Fluminense",
    "Cruzeiro",
    "Chapecoense",
    "CSA",
    "Avaí",
)
print("\033[34m-=\033[m" * 35)
print(f"Os cinco primeiros colocados: \033[31m{', '.join(campeonato[:5])}\033[m")
print("\033[34m-=\033[m" * 35)
print(f"Os ultimos quatro colocados: \033[32m{', '.join(campeonato[-4:])}\033[m")
print("\033[34m-=\033[m" * 35)
print(f"Os times em ordem alfabética: \033[35m{', '.join(sorted(campeonato))}\033[m")
print("\033[34m-=\033[m" * 35)
print(
    f"O Chapecoense esta na \033[36m{campeonato.index('Chapecoense')+1}\033[mª posição"
)
print("\033[34m-=\033[m" * 35)
