from termcolor import colored

num = int(input("Digite um numero: "))

if num % 2 == 0:
    print("O numero é", colored("PAR", "cyan"))
else:
    print("O numero é", colored("IMPAR", "cyan"))
