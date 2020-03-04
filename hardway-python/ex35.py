from sys import exit


def gold_room():
    print("This room if full of gold. How much do you take?")

    choice = str(input("> "))
    while True:
        if choice.isnumeric():
            how_much = int(choice)
        else:
            gold_room()

        if how_much < 50:
            print("Nice, you're not greedy, you win!")
            exit()
        else:
            dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        print("1 - Take honey\n2 - Taunt bear\n3 - Open door")
        choice = int(input("> "))

        if choice == 1:
            dead("The bear looks at you then slaps your face off.")
        elif choice == 2 and not bear_moved:
            print("The bear has moved from the door")
            print("You can go through it now.")
            bear_moved = True
        elif choice == 2 and bear_moved:
            dead("The bear gest pissed off and chews your leg off.")
        elif choice == 3 and bear_moved:
            gold_room()
        else:
            print("You can only open the door if the bear has moved")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    print("1 - Flee for your life\n2 - Eat your head")

    choice = int(input("> "))

    if choice == 1:
        start()
    elif choice == 2:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit()


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    print("1 - Left door\n2 - Right door")
    choice = int(input("> "))

    if choice == 1:
        bear_room()
    elif choice == 2:
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
