frase = str(input("Digite uma frase: ")).strip().lower()

print(f"\nA letra A aparece: {frase.count('a')} vezes")

print(f"A letra A aparece pela primeira vez em: {frase.find('a')+1}")

print(f"A letra A aparece pela ultima vez em: {frase.rfind('a')+1}")

print("\nComprimento da string da frase:", len(frase))

