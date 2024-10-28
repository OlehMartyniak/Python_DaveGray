def hello_world():
    print("Hello World!")

hello_world()

# def sum(num1, num2):
#     return num1 + num2



def sum(num1 = 0, num2 = 0): # якщо не вкласти аргументи то за замовчуванням вони дорівнюватимуть 0
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

total = sum(2,3)
print(total)



# якщо ми не знаємо кількості аргументів які передамо в функцію, то використовуємо *args що поверне нам tuple
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("John","Boe")
# ('John', 'Boe')
# <class 'tuple'>



# якщо використати **args то зможемо передати також довільну кількість аргументів, які повернуться як dictionary
def mult_items(**args):
    print(args)
    print(type(args))

mult_items(first = "Oleg", last = "Mart")
# {'first': 'Oleg', 'last': 'Mart'}
# <class 'dict'>