users = ['Mike','Erren','Barry']

data = ['Oleh', 26, False]

emptylist = []

print('Mike' in users)
# true


print(users[0])
# Mike
print(users[-2])
# Erren
print(users.index('Barry'))
# 2
print(users[0:2])
# ['Mike', 'Erren']
print(users[0:])
# ['Mike', 'Erren', 'Barry']
print(len(users))
# 3

# додаємо в лист нового юзера - append
users.append('Mikasa')
print(users)
# ['Mike', 'Erren', 'Barry', 'Mikasa']

# об'єднуємо два листи - +=
users += ['Alan','Moe']
print(users)
# ['Mike', 'Erren', 'Barry', 'Mikasa', 'Alan', 'Moe']

# ще один спосіб розширити лист - extend
users.extend(['Jeremy','Hagrid'])
print(users)
# ['Mike', 'Erren', 'Barry', 'Mikasa', 'Alan', 'Moe', 'Jeremy', 'Hagrid']

# додаємо інфо на конкретний індекс в лист - insert
users.insert(0,'Harvey')
print(users)
# ['Harvey', 'Mike' ...]

# додаємо кількі позицій в зазначений індекс (2)
users[2:2] = ['Alastor','Drew']
print(users)
# ['Harvey', 'Mike', 'Alastor', 'Drew', 'Erren'...]

# заміняємо інфо за індексом (2,3)
users[2:3] = ['Carl','Rick']
print(users)
# ['Harvey', 'Mike', 'Carl', 'Rick', 'Drew'...]

# видаляємо інфо з листа за назвою - remove()
users.remove('Harvey')
print(users)
# ['Mike', 'Carl', 'Rick'...]

# видяляємо останній індекс в листі - pop()
users.pop()
print(users)
# last index 'Hagrid' was deleted

# видаляємо інфо за конкретним індексом - del[]
del users[0]
print(users)
# 'Mike' was deleted

# можемо видалити також весь лист - del
# del data
# print(data)
# NameError: name 'data' is not defined

# можемо очистити лист - clear()
data.clear()
print(data)
# []

# сортування інфо за алфавітом - sort()
users.sort()
print(users)
# ['Alan', 'Barry', 'Carl', 'Drew'...]

# якщо наприклад один з елементів інфо записаний з малої літери, тоді потрібно застосувати наступне - sort(key=str.lower), інакше це інфо розміститься в кінці листа

users[1:2] = ['dany']
users.sort(key=str.lower)
print(users)
# ['Alan', 'Carl', 'dany', 'Drew'...]



nums = [5,36,86,7,2]

nums.reverse()
print(nums)
# [2, 7, 86, 36, 5]

nums.sort()
print(nums)
# [2, 5, 7, 36, 86]

nums.reverse()
print(nums)
# [86, 36, 7, 5, 2]

nums.sort(reverse=True)
print(nums)
# [86, 36, 7, 5, 2]

# створення копій
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]




# Tuples - very much like lists (arrays) but they cannot be changed

mytuple = tuple(('Oleg',26,True))

anothertuple = (2,5,8)

print(mytuple)
# ('Oleg', 26, True)
print(type(mytuple))
# <class 'tuple'>


# Хоча ми не можемо змінювати існуючі tuple, ми можемо створювати нові на основі існуючих:

# 1) створимо лист на основі tuple
newlist = list(mytuple)
# 2) додамо в цей лист нове значення
newlist.append('Barry')
# 3) створимо новий tuple на основі листа
newtuple = tuple(newlist)

print(newtuple)
# ('Oleg', 26, True, 'Barry')


