person = "Oleh"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")
# Oleh has 3 coins left.

message = "\n%s has %s coins left." % (person,coins)
print(message)
# Oleh has 3 coins left.

message1 = "\n{} has {} coins left.".format(person,coins)
print(message1)
# Oleh has 3 coins left.

message2 = "\n{1} has {0} coins left.".format(coins,person)
print(message2)
# Oleh has 3 coins left.

player = { "person": "Mike", "coins": 3 }
message3 = "\n{person} has {coins} coins left.".format(**player)
print(message3)
# Mike has 3 coins left.


#############################
# f-strings

message4 = f"\n{person} has {coins} coins left."
print(message4)
# Oleh has 3 coins left.

message5 = f"\n{person.lower()} has {2 * 5} coins left."
print(message5)
# oleh has 10 coins left.

message6 = f"\n{player['person']} has {2 * 5} coins left."
print(message6)
# Mike has 10 coins left.
