from datetime import date

print("\033[34m+\033[m" * 60)
print("\033[32m Avaliação de Categoria \033[m")
print("\033[34m=\033[m" * 60)

ano = int(input("Digite a sua data de nascimento: "))

idade = date.today().year - ano

if idade <= 9:
    print(f"O atleta tem {idade} anos")
    print("Categoria: \033[32mMIRIM\033[m")
elif 14 >= idade:
    print(f"O atleta tem {idade} anos")
    print("Categoria: \033[33mINFANTIL\033[m")
elif 19 >= idade:
    print(f"O atleta tem {idade} anos")
    print("Categoria: \033[34mJUNIOR\033[m")
elif 25 >= idade:
    print(f"O atleta tem {idade} anos")
    print("Categoria: \033[35mSENIOR\033[m")
else:
    print(f"O atleta tem {idade} anos")
    print("Categoria: \033[36mMASTER\033[m")
