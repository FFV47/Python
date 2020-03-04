print("\033[35m-=\033[m" * 20)
print("\033[32m Analisador de Triângulos \033[m")
print("\033[35m-=\033[m" * 20)

print("\033[33mDigite o comprimento de três segmentos de reta a seguir\033[m\n")
a = float(input("Digite o segmento A: "))
b = float(input("Digite o segmento B: "))
c = float(input("Digite o segmento C: "))


if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b):
    print("Os segmentos podem formar um triangulo ", end="")
    if a == b == c:
        print("\033[32mEQUILATERO\033[m")
    elif a == b or b == c or a == c:
        print("\033[34mISOSCELES\033[m")
    else:
        print("\033[35mESCALENO\033[m")
else:
    print("Os segmentos não podem formar um triangulo")
