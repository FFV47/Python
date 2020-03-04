exp = str(input("Digite uma expressão matemática: "))

left = exp.count("(")
right = exp.count(")")

print("\033[34m-=\033[m" * 40)
if left == right:
    print("\033[32mA expressão está correta !!!\033[m")
else:
    print("\033[31mA expressão está errada !!!\033[m")
