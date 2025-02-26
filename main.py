def home():
    answer = ""
    print("You are home")
    options = ["Sleep", "Road"]
    while  answer not in options:
        answer = input("Do you want to sleep or go down the road?\n").title()
        if answer == "Sleep":
            home()
        if answer == "Road":
            road()

def road():
    answer = ""
    print("You are walking down the road where would you like to go?")
    options = ["Shop", "Forest", "Friend"]
    while answer not in options:
        answer = input("Shop, Forest or Friend\n").title()
        if answer == "Shop":
            shop()
        if answer == "Forest":
            forest()
        if answer == "Friend":
            friend()

def shop():
    print("You are at the shop")
    answer = ""
    options = ["Eat", "Home"]
    while answer not in options:
        answer = input("Would you like to eat something or go home?\n").title()
        if answer == "Home":
            home()
        if answer == "Eat":
            eat()
def eat():
    print("You ate something and you got tired and went home")
    home()
def forest():
    print("You are walking in the forest...")
    print("What was that!")
    answer = ""
    options = ["Run", "Climb", "Hide"]
    while answer not in options:
        answer = input("There is something coming. Do you Run, Climb or hide\n").title()
        if answer == "Run":
            run()
        if answer == "Climb":
            climb()
        if answer == "Hide":
            hide()
def friend():
    print("You are at your friend")
    answer = ""
    options = ["Home","Play"]
    while answer not in options:
        answer = input("Would you like to play or go home?\n").title()
        if answer == "Home":
            home()
        if answer == "Play":
            play()


def play():
    print("You and our friend play around until you are tired and go home")
    home()

def run():
    print("Turns out it was a massive bear. It saw you as a target when you ran")
    print("It caught you and you died in the forest you had no business being in")
    answer = ""
    options=["Yes","No"]
    while answer not in options:
        answer = input("Would you like to try again?\n").title()
        if answer == "Yes":
            home()
        if answer == "No":
            print("I hope you had fun\nBye!")
def climb():
    print("Turns out it was a bear and it can climb better than what you can...")
    print("It caught you because you had nowhere to go. Just watching the bear climb up easier than we get out of bed")
    answer = ""
    options = ["Yes", "No"]
    while answer not in options:
        answer = input("Would you like to try again?\n").title()
        if answer == "Yes":
            home()
        if answer == "No":
            print("I hope you had fun\nBye!")
def hide():
    print("Turns out it was a bear. You can hear it's heavy breathing from the bush you are hiding in.")
    print("You wait in the bush until the bear leaves. You can see a freshly dug hole under the trunk of tree.")
    answer = ""
    options = ["Yes", "No"]
    while answer not in options:
        answer = input("Do you want to crawl in there and see what it is?\n").title()
        if answer == "Yes":
            crawl()
        if answer == "No":
            print("You decide to go home.")
            home()
def crawl():
    print("You found treasure in the hole.")
    print("YOU WIN!")
home()
