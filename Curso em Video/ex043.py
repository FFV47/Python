print("\033[34m+\033[m" * 60)
print("\033[32mCalculo de IMC\033[m")
print("\033[34m=\033[m" * 60)

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em m: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é \033[35m{imc:.1f}\033[m e você esta abaixo do peso.")
elif 25 > imc >= 18.5:
    print(f"Seu IMC é \033[35m{imc:.1f}\033[m e você esta no peso ideal.")
elif 30 > imc >= 25:
    print(f"Seu IMC é \033[35m{imc:.1f}\033[m e você esta com sobrepeso.")
elif 40 > imc >= 30:
    print(f"Seu IMC é \033[35m{imc:.1f}\033[m e você esta obeso.")
else:
    print(f"Seu IMC é \033[35m{imc:.1f}\033[m e você esta com obesidade mórbida")
