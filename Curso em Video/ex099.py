from time import sleep


def maior(*num):
    print("-=" * 25)
    print("Analisando os valores passados...")
    for i in num:
        print(f"{i} ", end="")
        sleep(0.4)
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior valor informado foi {max(num,default=0)}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print()
