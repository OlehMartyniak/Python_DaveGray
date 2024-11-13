# Higher Order Function - is a function that takes one or more functions  as
# arguments or a function that returns a function as it's result



# For example function map() which iterates through a list and takes lambda as it's argument
# В цьому випадку ф-ція map() буде проходитись по листу numbers і передавати його індекси в ф-цію lambda як num
numbers = [2,4,6,8,10]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums)) # [4, 16, 36, 64, 100]




# filter() function filrets out any results that do not pass our requirements
# в даному випадку ми повертатимемо тільки непарні (odd) числа

numbers2 = [3,7,8,9,11,12]

odd_numbers = filter(lambda num: num % 2 != 0, numbers2)

print(list(odd_numbers)) # [3, 7, 9, 11]



# reduce() також дозволяє пройтись по листу і в даному випадку додати всі числа в ньому
from functools import reduce

numbers3 = [1,3,6,10]

total = reduce(lambda acc, curr: acc + curr, numbers3)

print(total) # 20



# однак такий ж результат як з reduce() можна досягти легшим методом з допомогою ф-ції sum()

print(sum(numbers3)) # 20



# все ж reduce() можна використати для більш складних завдань, наприклад вирахувати к-сть букв в листі
names = ["Oleh", "Bon Jovi", "Messershmidt"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count) # 24


