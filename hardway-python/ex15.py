from sys import argv

filename = argv[1]

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())
txt.close()  # fecha o arquivo aberto depois de usa-lo

print(f"Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
print(txt_again.writable())
print(txt_again.encoding)
txt_again.close()
