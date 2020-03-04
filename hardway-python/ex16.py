from sys import argv

filename = argv[1]

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")

filename_before = open(filename).read()  # salvo o conteudo do arquivo como uma string

print("Opening the file...")
target = open(
    filename, "w+"
)  # O modo de escrita ja trunca o arquivo(apaga o conteudo), logo não é necessário truncar se usar esse modo

# print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}\n")

print("The file was:")
print(filename_before)
print("And now:")
# target = open(filename)
print(target.read())


print("And finally, we close it.")
target.close()
