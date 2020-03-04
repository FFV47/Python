from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")


current_file = open(input_file)

print("First let's print the whole file:\n")
print(1, current_file.readline())
print(2, current_file.readline())
print(3, current_file.readline())
print(4, current_file.readline())
print(5, current_file.readline())
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:\n")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)