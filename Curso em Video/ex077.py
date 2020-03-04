from random import randint

coleçao = (
    "Python",
    "Curso em Video",
    "Diolinux",
    "Manjaro",
    "Debian",
    "Ubuntu",
    "Fedora",
    "Redhat",
    "Opensuse",
    "Archlinux",
)

for palavra in coleçao:
    print(f"\nNa palavra {palavra.upper()} temos as vogais:", end=" ")
    print(f"\033[{randint(31,36)}m", end="")
    for vogal in palavra:
        if vogal.upper() in "AEIOU":
            print(f"{vogal.upper()}", end=" ")
    print("\033[m", end="")
print("\n")
