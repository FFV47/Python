print("let's practice everything.")
print("You'd need to know 'bout escapes with \\ that do:")
print("\n newlines and \t tabs")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("-" * 40)
print(poem)
print("-" * 40)


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
lista = secret_formula(start_point)
beans, jars, crates = secret_formula(start_point)
print(lista)

print(f"With a starting point of: {start_point}")
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
print("We'd have {} beans, {} jars, and {} crates".format(*lista))
