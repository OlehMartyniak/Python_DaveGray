value = 1
while value <= 10:
    print(value)
    if value ==5:
        break
    value += 1
# 1 2 3 4 5 6 7 8 9 10

value2 = 1
while value2 <= 10:
    value2 += 1
    if value2 == 5:
        continue # continue пропустить умову (число 5) і продовжить цикл
    print(value2)
else:
    print("Value is now equal to " + str(value2))
# 2 3 4 6 7 8 9 10 11

names = ["Oleh","Layla","John"]
for x in names:
    print(x)
# Oleh Layla John

for x in names:
    if x == "Layla":
        break
    print(x)
# Oleh

for x in names:
    if x == "Layla":
        continue
    print(x)
# Oleh John

for x in range(3):
    print(x)
# 0 1 2

for x in range(2,4):
    print(x)
# 2 3

for x in range(5,26,5):
    print(x)
# 5 10 15 20 25

names = ["Oleh","Layla","John"]
actions = ["codes","eats","sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + "!")
# Oleh codes! Oleh eats! Oleh sleeps! Layla codes! Layla eats! Layla sleeps! John codes! John eats! John sleeps!

for action in actions:
    for name in names:
        print(name + " " + action + "!")
# Oleh codes! Layla codes! John codes! Oleh eats! Layla eats! John eats! Oleh sleeps! Layla sleeps! John sleeps!