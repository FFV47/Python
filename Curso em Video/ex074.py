from random import randint

# tupla = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)

tupla = ()
for c in range(5):
    tupla += (randint(0, 10),)
print(tupla)

for p, i in enumerate(tupla):
    print(f"{i}, " if p != len(tupla) - 1 else f"{i}", end="")

# maior = menor = tupla[0]
# print(tupla)
# for p, i in enumerate(tupla):
#     print(f"{i}, " if p != len(tupla) - 1 else f"{i}", end="")
#     if i > maior:
#         maior = i
#     elif i < menor:
#         menor = i

# print(f"\n\nMaior: {maior}")
# print(f"Menor: {menor}")

print(f"\nMaior: {max(tupla)}")
print(f"Menor: {min(tupla)}")
