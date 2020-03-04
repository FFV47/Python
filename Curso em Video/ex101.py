def voto(nasc):
    from datetime import date

    idade = date.today().year - nasc
    if 18 <= idade <= 65:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO NEGADO"


# Main
data = int(input("Data de nascimento: "))
print(voto(data))
