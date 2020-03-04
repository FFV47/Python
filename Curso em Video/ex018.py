import math

ang_deg = float(input("Digite um valor para o angulo: "))

ang_rad = math.radians(ang_deg)

print(
    f"\nSeno de {ang_deg} = {math.sin(ang_rad):.3f} \nCosseno de {ang_deg} = {math.cos(ang_rad):.3f} \nTangente de {ang_deg} = {math.tan(ang_rad):.3f}"
)
