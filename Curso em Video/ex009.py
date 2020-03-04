num = int(input("Digite um numero para a tabuada: "))

print("-" * 12)
for i in range(1, 11):
    print(f"{i:2} x {num} = {i*num}")
print("-" * 12)
