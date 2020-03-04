from random import randint
from time import sleep

numeros = list()


def sorteio(numeros):

    print("Sorteando 5 valores da lista:", end=" ")
    for i in range(5):
        n = randint(0, 10)
        print(f"{n}", end=" ")
        numeros.append(n)
        sleep(0.4)
    print("PRONTO!")


def somaPar(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f"Somando os valores pares de {numeros}, temos {soma}", end=" ")
    print()


sorteio(numeros)
somaPar(numeros)
help(sorteio)
