"""Primeiro Método"""

num = input("Digite um numero de 0 a 9999: ").strip()

print("\nUnidade: ", num[3])
print("Dezena: ", num[2])
print("Centena: ", num[1])
print("Milhar: ", num[0])

"""Segundo Método"""

num_int = int(num)

u = num_int // 1 % 10
d = num_int // 10 % 10
c = num_int // 100 % 10
m = num_int // 1000 % 10

print(f"\nUnidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")
