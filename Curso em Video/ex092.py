from datetime import datetime

cadastro = dict()

cadastro["Nome"] = str(input("Nome: "))
birth = int(input("Ano de Nascimento: "))
cadastro["Idade"] = datetime.now().year - birth
cadastro["CTPS"] = int(input("Carteira de Trabalho [0 se não tiver]: "))
if cadastro["CTPS"] != 0:
    cadastro["Ano de Contratação"] = int(input("Ano de Contratação: "))
    cadastro["Idade para se Aposentar"] = cadastro["Ano de Contratação"] - birth + 35
    cadastro["Salário"] = float(input("Salário: "))

print("-" * 60)

for k, v in cadastro.items():
    if k == "CTPS" and v == 0:
        print(f"{k}: {v}")
        break
    elif k == "Salário":
        print(f"{k}: R$ {v:.2f}")
    else:
        print(f"{k}: {v}")
print()
