from math import hypot

cat_adj = float(input("Digite o valor do cateto adjacente: "))
cat_opo = float(input("Digite o valor do cateto oposto: "))

print(f"O valor da hipotenusa do triangulo é: {hypot(cat_adj,cat_opo):.2f}")
