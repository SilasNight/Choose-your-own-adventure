"""
This was the first game I ever made. It was made as a joke game for my wife.

I updated a lot of this game to make it look better. I have improved a
lot since I first made it.
"""


def home() -> None:
    """
    This is the starting point for the game
    """
    answer = ""
    print("You are home")

    # I use this configuration often. It's to make sure that the user
    # chooses an option that can be used in the program
    options = ["Sleep", "Road"]
    while answer not in options:

        # Offer the user the choices they can pick
        print("Do you want to sleep or go down the road?")
        answer = input("Sleep or Road?\n").title()

    # Changing the seen depending on the choice made
    if answer == "Sleep":
        home()
    if answer == "Road":
        road()


def road() -> None:
    """
    This is the scene of the user walking down the road.
    """

    answer = ""
    options = ["Shop", "Forest", "Friend"]

    # Making sure I get a valid answer
    while answer not in options:
        print("You are walking down the road where would you like to go?")
        answer = input("Shop, Forest or Friend?\n").title()

    # Changing the scene depending on the choice made
    if answer == "Shop":
        shop()
    if answer == "Forest":
        forest()
    if answer == "Friend":
        friend()


def shop() -> None:
    """
    This is the shop scene for the game
    """

    print("You are at the shop")
    answer = ""
    options = ["Eat", "Home"]

    # Making sure the answer is valid
    while answer not in options:
        print("Would you like to eat something or go home?")
        answer = input("Eat or Home?\n").title()

    # Changing the scene depending on user choice
    if answer == "Home":
        home()
    if answer == "Eat":
        eat()


def eat() -> None:
    """
    This is the scene of the user eating at the shop
    """

    print("You ate something and you got tired and went home")

    # The user is sent home after eating.
    home()


def forest() -> None:
    """
    This is the scene of the user going to the forest
    """

    print("You are walking in the forest...")
    print("What was that!")
    answer = ""
    options = ["Run", "Climb", "Hide"]

    # Ensuring a valid answer
    while answer not in options:
        answer = input("There is something coming. Do you Run, Climb or Hide?\n").title()

    # Changing the action depending on user choice
    if answer == "Run":
        run()
    if answer == "Climb":
        climb()
    if answer == "Hide":
        hide()


def friend() -> None:
    """
    This scene is the user going to their friend
    """

    print("You are at your friend")
    answer = ""
    options = ["Home", "Play"]

    # Ensuring a valid answer
    while answer not in options:
        print("Would you like to play or go home?\n")
        answer = input("Play or Home?\n").title()

    # Changing the scene depending on the user choice
    if answer == "Home":
        home()
    if answer == "Play":
        play()


def play() -> None:
    """
    This is the action of the user choosing to play with their friend
    """

    print("You and our friend play around until you are tired and go home")

    # The user gets sent home after playing
    home()


def run() -> None:
    """
    This is the choice to run if the user is in the forest
    """

    print("Turns out it was a massive bear. It saw you as a target when you ran.")
    print("It caught you and you died in the forest you had no business being in.")
    answer = ""
    options = ["Yes", "No"]

    # This will ensure a valid answer
    while answer not in options:
        print("Would you like to try again?")
        answer = input("Yes or No?\n").title()

    # Asking the user if they want to restart the game or quit
    if answer == "Yes":
        home()
    if answer == "No":
        print("I hope you had fun\nBye!")


def climb() -> None:
    """
    This is the climbing scene for if the user chooses the climb option
    in the forest.
    """

    print("Turns out it was a bear and it can climb better than what you can...")
    print("It caught you because you had nowhere to go. Just watching the bear climb up easier than we get out of bed.")
    answer = ""
    options = ["Yes", "No"]

    # Ensures a valid answer from the user
    while answer not in options:
        print("Would you like to try again?")
        answer = input("Yes or No?\n").title()

    # Asks the user if they would like to play again.
    if answer == "Yes":
        home()
    if answer == "No":
        print("I hope you had fun\nBye!")


def hide() -> None:
    """
    This is the scene for if the user chooses to hide in the forest.
    """

    print("Turns out it was a bear. You can hear it's heavy breathing from the bush you are hiding in.")
    print("You wait in the bush until the bear leaves. You can see a freshly dug hole under the trunk of tree.")
    answer = ""
    options = ["Yes", "No"]

    # This ensures a valid answer
    while answer not in options:
        answer = input("Do you want to crawl in there and see what it is?\n").title()

    # This is to change the scene depending on user choice
    if answer == "Yes":
        crawl()
    if answer == "No":
        print("You decide to go home.")
        home()


def crawl() -> None:
    """
    This is the win condition.
    """
    print("You found treasure in the hole!")
    print("YOU WIN!")


if __name__ == "__main__":
    home()
