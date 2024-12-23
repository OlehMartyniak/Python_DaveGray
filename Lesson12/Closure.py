#  Closure is a function having access to the scope of its parent function after the parent function has returned

def parent_function(person):
    coins = 3

    def play_game():
        nonlocal coins # nonlocal дозволяє використовувати змінну з parent function
        coins -= 1 # coins = coins -1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")
    return play_game

tommy = parent_function("Tommy")
jenny = parent_function("Jenny")

tommy()
tommy()
jenny()