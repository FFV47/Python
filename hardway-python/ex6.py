people = 10
x = f"There are {people} types of people"

binary = "binary"
do_not = "don't"
y = f"Those who now {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said {x}")
print(f"I also said {y}")

hilarious = False
joke_evaluation = "Isn't that joke funny? {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
