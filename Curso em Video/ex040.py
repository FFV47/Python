print("\033[34m+\033[m" * 60)
print("\033[32m Avaliação de Notas \033[m")
print("\033[34m=\033[m" * 60)

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media < 5:
    print(f"Voce obteve média {media:.1f},\033[31m REPROVADO \033[m")
elif 6.9 >= media >= 5:
    print(f"Voce obteve média {media:.1f},\033[33m RECUPERAÇÃO \033[m")
else:
    print(f"Voce obteve média {media:.1f},\033[32m APROVADO \033[m")
