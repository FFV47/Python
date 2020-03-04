from termcolor import colored

vel = float(input("Digite a velocidade do carro: "))

if vel >= 80:
    print(
        colored("Você foi multado! Você deve pagar", "red"),
        colored(f"R$ {(vel-80) * 7:.2f}", "magenta", None, ["bold"]),
    )
else:
    print(colored("Você está abaixo do limite de velocidade", "yellow"))
