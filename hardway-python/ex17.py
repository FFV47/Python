from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file).read()

print(f"The input file is {len(in_file)} bytes long.")
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "w")  # Cria o arquivo se nao existir
out_file.write(in_file)
print(f"Copying from {from_file} to {out_file.name}.")

out_file.close()
