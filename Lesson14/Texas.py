# Custom module

from random import choice

capital = "Austin"
largest_city = "Houston"
slogan = "The Friendly State"

def randomfact():
    funfacts = [
        "Texas is nicknamed the Lone Star State for its former status as an independent republic.","Texas has a coastline on the Gulf of Mexico to the southeast.","It borders Louisiana to the east, Arkansas to the northeast, Oklahoma to the north, New Mexico to the west, and an international border with the Mexico.","The Lone Star can be found on the Texas state flag and the Texas state seal."
    ]
    index = choice("0123")
    # задаємо індекси доступні в dictionary funfacts

    return print(funfacts[int(index)])
    # ф-ція randomfact() буде друкувати один з рандомних (choice) індексів з funfacts

